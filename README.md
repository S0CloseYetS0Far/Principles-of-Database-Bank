# Principles of Database Bank

Practice site for **CS370 Introduction to Database** (Imam Mohammad Ibn Saud Islamic University): 236 questions from past midterms, finals and quizzes, sorted by chapter (1–9), with instant checking.

Open `index.html` in any browser. It is a single self-contained file that works offline.

Every question shows which exam it came from and where its answer came from:

| Label | Meaning |
|---|---|
| Official key | Answer key printed in the exam file |
| Graded paper | A student's paper the instructor marked |
| Marked + checked | Answer selected on a quiz screenshot, checked against the slides |
| From slides | No answer on the paper; taken from the chapter slides |
| Worked out | No answer on the paper; worked out from the question's own tables or diagram |

The full source list is at the bottom of the page.

## Editing the questions

Questions live in `src/bank.py`, the page template in `src/page.html`, and exam diagrams in `src/img/`. Rebuild with:

```bash
pip install pymupdf
python src/build.py
```

This regenerates `index.html`.
