import json, base64, pymupdf, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from bank import Q
HERE = os.path.dirname(__file__)

SOURCES = {
 "M23S":  ("Midterm, Summer 2023", "Exams/Mid/Mid-CS370-3rd-2023-MA.pdf", "Official model answer inside the file"),
 "M24_2": ("Midterm, 2nd semester 2024", "Exams/Mid/2024/Midterm_2nd_2024.pdf", "Official answer key inside the file"),
 "M23_1": ("Midterm, 1st semester 2023 (same paper as 2021)", "Exams/Mid/Midterm_S1_2023_Manal Alsabhan.pdf + Exams/Mid/Mid1-CS370-1st-2021-MA/", "Graded student papers, full marks on these parts"),
 "M24_1": ("Midterm, 1st semester 2024", "Exams/Mid/2024/Midterm_1st_2024.pdf", "No answers on the paper; answers from the slides"),
 "M25_2": ("Midterm, 2nd semester 2025", "Exams/Mid/2025/Midterm_2nd_2025.pdf", "No answers on the paper; answers from the slides and the diagram"),
 "M25_3": ("Midterm, 3rd semester 2025", "Exams/Mid/2025/Midterm_3rd_2025.pdf", "No answers on the paper; answers from the slides and the diagram"),
 "F23_1": ("Final, 1st semester 2023", "Exams/Final/2023/Final_1st_2023.pdf", "One answer boxed on the paper; the rest from the slides and the diagram"),
 "F24_1": ("Final, 1st semester 2024", "Exams/Final/2024/Final_1st_2024.pdf", "No answers on the paper; answers from the slides and worked out from the tables"),
 "F25_2": ("Final, 2nd semester 2025", "Exams/Final/2025/Final_2nd_2025.pdf", "No answers on the paper; answers from the slides and worked out from the tables"),
 "F25_3": ("Final, 3rd semester 2025", "Exams/Final/2025/Final_3rd_2025.pdf", "No answers on the paper; answers from the slides and worked out from the tables"),
 "Q23_2": ("Quiz 2, 2nd semester 2023 (Dr. Dalal)", "Exams/Quiz/2023/Quiz2_2nd_2023_Female_Dr.Dalal_Alduwaila.pdf", "Blackboard screenshots with selected answers; each one re-checked"),
 "Q24_S": ("Quiz 1, Summer 2024", "Exams/Quiz/2024/QUIZ1_SUMMER 2024.pdf", "Microsoft Forms screenshots with selected answers; checked against the slides"),
 "Q24_1": ("Quiz 1, 1st semester 2024", "Exams/Quiz/2024/Quiz1_1st_2024.pdf", "Blackboard screenshots with selected answers; checked against the slides (one corrected)"),
 "Q24_1b":("Quiz 2, 1st semester 2024", "Exams/Quiz/2024/Quiz2_1st_2024.pdf", "No answers on the paper; worked out from the tables"),
 "Q25_1": ("Quiz 1, 1st semester 2025/2026", "Exams/Quiz/2025/Quiz1-1st Semester 2025_2026.pdf", "No answers on the paper; answers from the slides"),
 "Q25_2": ("Quiz 1, 2nd semester 2025", "Exams/Quiz/2025/Quiz1_2nd_2025.pdf", "No answers on the paper; answers from the slides"),
 "Q25_3": ("Quiz 1, 3rd semester 2025", "Exams/Quiz/2025/Quiz1_3rd_2025.pdf", "No answers on the paper; answers from the slides and the diagram"),
 "Q25_3b":("Quiz 2, 3rd semester 2025", "Exams/Quiz/2025/Quiz2_3rd_2025.pdf", "No answers on the paper (the red mark on item 1 is a redaction); answers from the slides"),
 "Q26_2": ("Quiz 1, 2nd semester 2026", "Exams/Quiz/2026/Quiz1_2nd_2026.pdf", "Written questions; answers from the slides"),
 "Q22":   ("Quiz 1, Fall 2022", "Exams/Quiz/Quiz1-Fall2022/", "Graded student paper; answers taken from the parts marked correct"),
 "Q21":   ("Quiz 1, Fall 2021 (Ms. Amal Alamr)", "Exams/Quiz/Quiz1-Ms.AmalAlamr-Fall2021-cs370/", "Graded student paper; both MCQs were marked wrong, so the correct choice is from the slides"),
}
SKIPPED = [
 "Drawing questions (ER/EER diagrams for the restaurant, library, bank, NFL, motor-vehicle branch, university and bookstore cases) — there's no single right answer to check automatically.",
 "Mapping questions whose diagram is too blurry or cut off (insurance company, hospital, Father/Child, Lecturer/Course).",
 "Quiz 1, 3rd semester 2024 — the file contains question stems only, no answer choices.",
 "Questions where the photo is cut off or the answer is genuinely ambiguous (e.g. the podcast 'Entity vs Instance' version in Quiz 1 2nd 2025, the 'NOT a type of data model' question in Quiz 1 Summer 2024, the Magazine normalization in Final 1st 2024).",
 "The Arabic recollection sheet on page 3 of Final_1st_2023.pdf.",
]
CHAPTERS = {
 1: ("Databases and Database Users", "CS1370_Chapter1.pdf"),
 2: ("Database System Concepts and Architecture", "CS1370_Chapter2.pdf"),
 3: ("Data Modeling Using the ER Model", "CS1370_Chapter3.pdf"),
 4: ("The Enhanced ER (EER) Model", "CS1370_Chapter4.pdf"),
 5: ("The Relational Model and Constraints", "CS1370_Chapter5.pdf"),
 6: ("ER/EER-to-Relational Mapping", "CS1370_Chapter6.pdf"),
 7: ("Relational Algebra and Calculus", "CS1370_Chapter7.pdf"),
 8: ("SQL: Definition, Constraints, Queries, Views", "CS370_Chapter8_DDL.pdf + CS370_Chapter8_DML_part2.pdf"),
 9: ("Functional Dependencies and Normalization", "CS1370_Chapter9.pdf"),
}

# embed images as compressed JPEG data URIs
imgs = {}
for q in Q:
    k = q.get("img")
    if k and k not in imgs:
        pix = pymupdf.Pixmap(os.path.join(HERE, "img", k + ".png"))
        if pix.alpha: pix = pymupdf.Pixmap(pix, 0)
        if pix.width > 1000:
            pix = pymupdf.Pixmap(pix, 1000, int(pix.height * 1000 / pix.width), None)
        imgs[k] = "data:image/jpeg;base64," + base64.b64encode(pix.tobytes("jpg", jpg_quality=82)).decode()

for i, q in enumerate(Q):
    q["id"] = f"c{q['ch']}-{i}"
    for s in q["s"]: assert s in SOURCES, s

data = dict(q=Q, src={k: dict(n=v[0], f=v[1], h=v[2]) for k, v in SOURCES.items()},
            ch={k: dict(n=v[0], f=v[1]) for k, v in CHAPTERS.items()}, img=imgs, skipped=SKIPPED)
tpl = open(os.path.join(HERE, "page.html"), encoding="utf-8").read()
page = tpl.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
standalone = "<!doctype html>\n<html lang=\"en\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n" + page + "\n</html>"
open(os.path.join(HERE, "..", "index.html"), "w", encoding="utf-8").write(standalone)
from collections import Counter
print(len(Q), "questions", dict(sorted(Counter(q["ch"] for q in Q).items())), "size", len(page)//1024, "KB")
