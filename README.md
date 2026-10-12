# Python Bootcamp — Team <team number>

## Team Members

Name | GitHub | Folder |
Nguyễn Quang Khải | ng-wngkh07 | ng_wngkh07 |
Võ Nguyễn Hoàng Bách | hoagpac | hoagpac |
Nguyễn Tuấn Minh | ntuanminh53-hub | ntuanminh53_hub |
Bùi Minh Trí| mtrstapcode | mtrstapcode |
Lê Bá Hoàng Tú | ferb132| ferb132 |
Nguyễn Gia Huy | cknotk249 | cknotk249 |

## Directory Structure

```text
python-bootcamp/
├── README.md
├── PROGRESS.md
├── members/
│   └── <username>/
│       ├── w1/
│       ├── w2/
│       └── w3/
├── shared/
└── tests/
```

- `members/`: individual exercises; each member writes code in their own folder.
- `shared/`: the team’s shared code.
- `tests/`: the test suite provided by the instructor.
- `PROGRESS.md`: progress, issues, PRs, reviewers, test results, and actual hours spent.

Personal folder names use GitHub usernames with hyphens replaced by underscores.

## Week 1 Exercises

Deadline: **10:00 PM on October 15, 2026**.

| Exercise | File | Description |
|---|---|---|
| W1-1 | `grades.py` | Grade statistics: min, max, mean, and median. |
| W1-2 | `text_tools.py` | Count words and return the top-k most frequent words. |
| W1-3 | `rules.py` | Check thesis registration eligibility and provide reasons for ineligibility. |
| W1-4 | `translate.py` | Translate the assigned C++ function into Python. |
| W1-5 | `timetable.py` | Group courses by day and sort each course list. |

## Environment and Running Tests

Use Python 3.12. Run the following commands from the **repository root**:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install pytest ruff
```

Test one member’s Week 1 exercises:

```bash
python3 -m pytest -q python-bootcamp/tests/test_w1.py --member <personal_folder> --variant <variant_number>
```

The `--member` and `--variant` options require the instructor-provided `conftest.py`. Use the variant number assigned by the team and follow the test suite’s instructions.

Check the entire bootcamp:

```bash
python3 -m ruff check python-bootcamp
python3 -m pytest -q python-bootcamp
```

## Homework Workflow

1. Update `main` and create a branch named `py/w1-<github-username>`.
2. Open a Week 1 issue, assign it to yourself, and add the `python-hw` and `w1` labels.
3. Complete one exercise at a time and commit after each exercise; make at least five commits during the week.
4. Use clear commit messages, for example: `feat(py-w1): W1-2 word counter`.
5. Run checks and push daily.
6. Open a PR titled `py-w1: <username>`, include `Closes #<issue>`, and request your reviewer.
7. Address review feedback; merge when the PR is approved and CI passes.
8. Update your personal row in `PROGRESS.md`.

## Reviews

Reviewers check test results, correctness, edge cases, Python style, variable names, and docstrings.

Each review includes at least one **Question**, one **Suggestion**, and one **Praise**. Approve only when you understand the code and the checks pass.

The Week 1 review rotation for a four-member team is: **1 → 2 → 3 → 4 → 1**. Larger teams record their agreed review rotation in the issue.

## Week 1 Completion

- All individual PRs and T-W1 tasks are completed.
- Individual PRs are approved by the assigned reviewer and merged into `main`.
- CI passes.
- `PROGRESS.md` contains accurate information for every member.
- The Tech Lead pushes the `py-w1-done` tag.
- The team repository link is submitted to the LMS before the deadline.
