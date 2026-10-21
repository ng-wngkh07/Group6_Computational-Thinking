import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from members.ntuanminh53_hub.w1 import grades, rules, text_tools, timetable, transposematrix


def test_summary_basic_and_odd():
    res = grades.summary([8.0, 3.0, 7.0])
    assert res == {"min": 3.0, "max": 8.0, "mean": 6.0, "median": 7.0}


def test_summary_empty_raises_value_error():
    with pytest.raises(ValueError):
        grades.summary([])


def test_thesis_boundary_conditions():
    assert rules.can_register_thesis(120, 2.0) is True
    assert rules.can_register_thesis(119, 2.0) is False
    assert rules.can_register_thesis(120, 1.99) is False
    assert rules.missing(120, 2.0) == []
    assert len(rules.missing(110, 1.5)) == 2


def test_word_count_and_top_k():
    text = "apple, banana! apple? orange; banana: apple."
    counts = text_tools.word_count(text)
    assert counts["apple"] == 3
    assert counts["banana"] == 2
    assert counts["orange"] == 1
    assert text_tools.top_k(text, 2) == [("apple", 3), ("banana", 2)]


def test_top_k_alphabetical_tie():
    text = "dog cat bird dog cat"
    assert text_tools.top_k(text, 2) == [("cat", 2), ("dog", 2)]


def test_timetable_grouping():
    entries = [("Math", "Mon"), ("Physics", "Tue"), ("English", "Mon")]
    grouped = timetable.by_day(entries)
    assert grouped["Mon"] == ["English", "Math"]
    assert grouped["Tue"] == ["Physics"]


def test_transpose_matrix():
    mat = [[1, 2, 3], [4, 5, 6]]
    assert transposematrix.transpose(mat) == [[1, 4], [2, 5], [3, 6]]
    assert transposematrix.transpose([]) == []
