# Instructor Materials: Source and Usage

Imported on October 12, 2026 from the course's public repository:

https://github.com/CSC10014-at-fit-hcmus/public_materials/tree/4c1b2d08f52d179ffb8538f617f16e140f4a6fd2/python-bootcamp

Source revision: `4c1b2d08f52d179ffb8538f617f16e140f4a6fd2`.

The six files below are unchanged copies of the instructor's materials. This document is a local usage guide, not an instructor-provided file.

## Imported Files

| File | Purpose |
|---|---|
| `tests/conftest.py` | Adds `--member` and `--variant`, and imports a member's exercise modules. |
| `tests/test_w1.py` | Five test functions covering Week 1 exercises. |
| `tests/test_w2.py` | Three test functions covering the Task model, CSV/JSON handling, and the custom exception. |
| `tests/test_w3.py` | Three test functions covering date parsing, log analysis, and the CLI. |
| `samples/tasks.csv` | Valid task data used by Week 2 and Week 3 tests. |
| `samples/tasks_bad.csv` | Deliberately invalid data; Week 2 expects a ValueError referring to line 3. |

The selected upstream folder contains no README, solutions, CI workflow, or tests for additional W1-4 variants.

## Current Project Layout

This Git repository already uses the bootcamp directory as its root. Do not add another nested `python-bootcamp/` directory solely to match the tutorial's example paths.

Run commands from this repository root. A GitHub repository name such as `python_bootcamp` does not change these relative paths.

The project currently has these six personal folders:

- `members/cknotk249/`
- `members/ferb132/`
- `members/hoagpac/`
- `members/mtrstapcode/`
- `members/ng_wngkh07/`
- `members/ntuanminh53_hub/`

The `ferb132` folder was added while the import was being prepared and is included in the preserved project files. The member-to-variant assignment still needs to be recorded by the team; do not infer it from the order of names alone.

Each member creates `w1/`, `w2/`, and `w3/` under their own folder. Instructor tests import modules from `members.<folder>.wN.<module>`.

The existing project README uses example paths starting with `python-bootcamp/`. With the current repository layout, replace that prefix with the actual root-relative paths, such as `tests/test_w1.py`. The original README is preserved during this import.

## Running Tests

Use Python 3.12 and install pytest in your project's virtual environment.

Example for a member assigned variant 1:

```bash
python -m pytest -q tests/test_w1.py --member ng_wngkh07 --variant 1
```

Replace the example folder and variant with the team leader's actual assignment; this example does not assign that member variant 1.

For later weeks:

```bash
python -m pytest -q tests/test_w2.py --member YOUR_FOLDER
python -m pytest -q tests/test_w3.py --member YOUR_FOLDER
```

For Week 1, check only the Week 1 test file. Selecting every week for a member also runs tests for unfinished Week 2 and Week 3 modules.

### Important Test Behavior

- Omitting `--member` skips all 11 test functions. A successful command with only skipped tests is not evidence that anyone's homework passes.
- `--member` selects one member. CI must explicitly select each member to check the whole team.
- W1-4 supports binary search (1), insertion sort (2), transpose (3), and primes (4).
- The source uses an `else` branch for the primes test. Therefore `--variant 5` or `6` also checks `primes_up_to`; it does not test a fifth or sixth algorithm.
- Keep instructor files unchanged. Agree with the instructor on testing additional variants; record any separate tests and their commands.
- Passing these tests does not check every requirement in the tutorial. For example, the insertion-sort test checks returned values but does not verify in-place mutation.

## Exact Week 1 Module and Function Names

| Module | Functions expected by instructor tests |
|---|---|
| `w1/grades.py` | `summary(scores)` |
| `w1/text_tools.py` | `word_count(text)`, `top_k(text, k)` |
| `w1/rules.py` | `can_register_thesis(credits, gpa)`, `missing(credits, gpa)` |
| `w1/translate.py` | `binary_search(a, key)`, `insertion_sort(a)`, `transpose(matrix)`, or `primes_up_to(n)`, according to the assigned variant |
| `w1/timetable.py` | `by_day(pairs)` |

Implement the assigned function in `translate.py`; a member is not required to implement all four variants.

The test also checks for a module or callable docstring. For `missing(118, 3.1)`, the exact expected result is `["need 2 more credits"]`.

## Verification Boundary

The import is checked against the source file hashes, and the test suite is checked for syntax and collection. These checks do not mean the homework is complete. At import preparation time, personal folders contained only placeholders and no exercise implementations.
