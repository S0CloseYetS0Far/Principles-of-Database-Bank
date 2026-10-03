**English** | [العربية](README.md)

# Principles of Database Bank

Practice site for **CS370 Introduction to Database** (Imam Mohammad Ibn Saud Islamic University): 236 questions from past midterms, finals and quizzes, sorted by chapter (1–9), with instant checking.

## How to use

### Open it

1. On this repository's page, click **Code → Download ZIP**, then unzip it. (Or, if you use git: `git clone` the repository.)
2. Double-click `index.html`. It opens in your browser.

That's it. It is a single file with no installation, and it works offline.

### Practice

- **Pick a chapter:** the tabs at the top (**Ch 1** to **Ch 9**, or **All**). Each tab shows how many questions you've done and how many you got right.
- **Answer:** click a choice. The correct answer turns green; if you picked wrong, your choice is crossed out in red. A short explanation appears underneath.
- **Move between questions:** **Next →** and **← Previous**, or the arrow keys.
- **Keyboard shortcuts:** `a`–`d` (or `1`–`4`) to choose, `t` / `f` for True/False, `←` `→` to move.
- **Answer sheet:** the grid on the right works like the exam's answer table. It fills in as you go (green = correct, red = missed). Click any box to jump to that question.
- **Written questions** (SQL, mapping, normalization): write your answer on paper first, click **Show model answer**, then mark yourself with **I got it** or **I missed it**.

### Filter and review

- **Show** menu:
  - **All questions**
  - **Not answered yet**
  - **Ones I missed** (good for revising before an exam)
  - **Multiple choice & T/F only**
  - **Written answers only**
- **Shuffle:** randomizes the question order.
- **Clear answers:** resets your answers for the chapter you're on (it asks before clearing).

Your progress is saved in the browser on your device. It won't carry over to another browser or device.

## Where the answers come from

Every question shows which exam it came from and where its answer came from:

| Label | Meaning |
|---|---|
| Official key | Answer key printed in the exam file |
| Graded paper | A student's paper the instructor marked |
| Marked + checked | Answer selected on a quiz screenshot, checked against the slides |
| From slides | No answer on the paper; taken from the chapter slides |
| Worked out | No answer on the paper; worked out from the question's own tables or diagram |

The full source list is at the bottom of the page. **Worked out** answers are the ones most worth double-checking.

## Editing the questions

Questions live in `src/bank.py`, the page template in `src/page.html`, and exam diagrams in `src/img/`. Rebuild with:

```bash
pip install pymupdf
python src/build.py
```

This regenerates `index.html`.
