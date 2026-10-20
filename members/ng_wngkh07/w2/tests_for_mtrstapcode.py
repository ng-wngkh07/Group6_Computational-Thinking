import pytest

from members.mtrstapcode.w1 import grades, rules, text_tools, timetable, translate


def test_summary_odd_number_of_scores():
    assert grades.summary([9, 2, 4]) == {
        "min": 2,
        "max": 9,
        "mean": 5.0,
        "median": 4,
    }


def test_empty_summary_raises():
    with pytest.raises(ValueError):
        grades.summary([])


def test_top_k_tie_breaks_alphabetically():
    assert text_tools.top_k("z a z a b", 2) == [("a", 2), ("z", 2)]


def test_thesis_boundaries():
    assert rules.can_register_thesis(120, 2.0)
    assert not rules.can_register_thesis(119, 2.0)
    assert not rules.can_register_thesis(120, 1.99)


def test_missing_credits_reason():
    assert rules.missing(118, 3.1) == ["need 2 more credits"]


def test_timetable_sorts_each_day():
    assert timetable.by_day(
        [
            ("Z", "Mon"),
            ("A", "Mon"),
            ("B", "Tue"),
        ]
    ) == {"Mon": ["A", "Z"], "Tue": ["B"]}


def test_primes_required_public_function():
    assert translate.primes_up_to(10) == [2, 3, 5, 7]
    assert translate.primes_up_to(1) == []
