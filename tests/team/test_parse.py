from datetime import date
from pathlib import Path

import pytest

from shared.contract import Task
from shared.study_planner.parse import parse_csv

ROOT = Path(__file__).resolve().parents[2]


def test_sample_returns_shared_tasks():
    assert parse_csv(ROOT / "samples/tasks.csv") == [
        Task("DS exam", 5, 6.0, date(2026, 10, 30)),
        Task("Assignment", 4, 1.5, date(2026, 10, 27)),
    ]


def test_bad_sample_reports_line_three():
    with pytest.raises(ValueError, match="line 3"):
        parse_csv(ROOT / "samples/tasks_bad.csv")


def test_quoted_unicode_title(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text(
        'title,importance,effort_h,deadline\n"Ôn tập, Python",4,1.5,2026-10-27\n',
        encoding="utf-8",
    )
    assert parse_csv(path)[0].title == "Ôn tập, Python"


@pytest.mark.parametrize(
    "row",
    [
        "Bad,3,1,2026-02-30",
        "Bad,3,-1,2026-10-30",
        "Bad,3,nan,2026-10-30",
        "Bad,3,1",
        "Bad,6,1,2026-10-30",
    ],
)
def test_invalid_record_reports_line(tmp_path, row):
    path = tmp_path / "bad.csv"
    path.write_text(
        "title,importance,effort_h,deadline\n" + row + "\n", encoding="utf-8"
    )
    with pytest.raises(ValueError, match="line 2"):
        parse_csv(path)


def test_header_only_returns_empty_list(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text("title,importance,effort_h,deadline\n", encoding="utf-8")
    assert parse_csv(path) == []


def test_empty_file_rejects_missing_header(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text("", encoding="utf-8")
    with pytest.raises(ValueError, match="line 1"):
        parse_csv(path)


def test_missing_file_preserves_exception(tmp_path):
    with pytest.raises(FileNotFoundError):
        parse_csv(tmp_path / "missing.csv")


def test_multiline_record_keeps_physical_line_numbers(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text(
        'title,importance,effort_h,deadline\n"Part one\npart two",3,1,2026-10-30\nBad,high,1,2026-10-30\n',
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="line 4"):
        parse_csv(path)
