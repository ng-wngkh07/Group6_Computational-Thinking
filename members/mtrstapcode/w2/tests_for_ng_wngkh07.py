try:
    from members.ng_wngkh07.W1 import grades, rules, text_tools, timetable, translate
except ModuleNotFoundError:
    from members.ng_wngkh07.w1 import grades, rules, text_tools, timetable, translate

# 1. Tests for grades.py

def test_grades_summary_empty():
    assert grades.summary([]) == {
        "min": 0,
        "max": 0,
        "mean": 0,
        "median": 0,
    }


def test_grades_summary_single_element():
    result = grades.summary([8.5])
    assert result == {
        "min": 8.5,
        "max": 8.5,
        "average": 8.5,
        "median": 8.5,
    }


def test_grades_summary_odd_count():
    result = grades.summary([9, 2, 4])
    assert result == {
        "min": 2,
        "max": 9,
        "average": 5.0,
        "median": 4,
    }


def test_grades_summary_even_count():
    result = grades.summary([10, 20, 30, 40])
    assert result == {
        "min": 10,
        "max": 40,
        "average": 25.0,
        "median": 25.0,
    }


def test_grades_summary_floats():
    result = grades.summary([7.5, 9.0, 6.0, 8.0])
    assert result["min"] == 6.0
    assert result["max"] == 9.0
    assert result["average"] == 7.625
    assert result["median"] == 7.75

# 2. Tests for rules.py

def test_can_register_thesis_boundary_and_above():
    assert rules.can_register_thesis(120, 2.0) is True
    assert rules.can_register_thesis(130, 3.5) is True


def test_can_register_thesis_insufficient_credits():
    assert rules.can_register_thesis(119, 2.0) is False
    assert rules.can_register_thesis(0, 4.0) is False


def test_can_register_thesis_insufficient_gpa():
    assert rules.can_register_thesis(120, 1.99) is False
    assert rules.can_register_thesis(150, 1.0) is False


def test_can_register_thesis_both_insufficient():
    assert rules.can_register_thesis(100, 1.5) is False


def test_missing_when_eligible():
    assert rules.missing(120, 2.0) == []
    assert rules.missing(135, 3.8) == []


def test_missing_credits_only():
    assert rules.missing(118, 3.1) == ["Chưa đủ 120 tín chỉ"]


def test_missing_gpa_only():
    assert rules.missing(125, 1.8) == ["Điểm GPA chưa đạt 2.0"]


def test_missing_both_reasons():
    reasons = rules.missing(100, 1.5)
    assert reasons == ["Chưa đủ 120 tín chỉ", "Điểm GPA chưa đạt 2.0"]

# 3. Tests for text_tools.py

def test_word_count_basic():
    text = "Hello, world! Hello; python: world?"
    assert text_tools.word_count(text) == {
        "hello": 2,
        "world": 2,
        "python": 1,
    }


def test_word_count_empty():
    assert text_tools.word_count("") == {}
    assert text_tools.word_count("   .,!?;:   ") == {}


def test_top_k_standard():
    text = "cat dog bird dog cat dog"
    assert text_tools.top_k(text, 2) == [("dog", 3), ("cat", 2)]


def test_top_k_alphabetical_tie_break():
    text = "zebra ant zebra ant bee"
    assert text_tools.top_k(text, 2) == [("ant", 2), ("zebra", 2)]


def test_top_k_invalid_or_zero_k():
    assert text_tools.top_k("some words here", 0) == []
    assert text_tools.top_k("some words here", -2) == []


def test_top_k_k_greater_than_vocab():
    text = "apple banana"
    assert text_tools.top_k(text, 5) == [("apple", 1), ("banana", 1)]


def test_top_k_empty_text():
    assert text_tools.top_k("", 3) == []

# 4. Tests for timetable.py

def test_timetable_by_day_empty():
    assert timetable.by_day([]) == {}


def test_timetable_by_day_single_entry():
    assert timetable.by_day([("Math", "Mon")]) == {"Mon": ["Math"]}


def test_timetable_by_day_multiple_days():
    pairs = [("CSC10014", "Mon"), ("MTH00003", "Tue"), ("PHY00001", "Wed")]
    expected = {
        "Mon": ["CSC10014"],
        "Tue": ["MTH00003"],
        "Wed": ["PHY00001"],
    }
    assert timetable.by_day(pairs) == expected


def test_timetable_by_day_sorts_courses_alphabetically():
    pairs = [
        ("ZOO101", "Mon"),
        ("BIO101", "Mon"),
        ("CHE101", "Mon"),
    ]
    assert timetable.by_day(pairs) == {"Mon": ["BIO101", "CHE101", "ZOO101"]}


def test_timetable_by_day_handles_duplicates():
    pairs = [("LAB1", "Fri"), ("LEC1", "Fri"), ("LAB1", "Fri")]
    assert timetable.by_day(pairs) == {"Fri": ["LAB1", "LAB1", "LEC1"]}

# 5. Tests for translate.py

def test_merge_sort_basic():
    arr = [5, 2, 9, 1, 6]
    translate.merge_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 5, 6, 9]


def test_merge_sort_already_sorted():
    arr = [1, 2, 3, 4, 5]
    translate.merge_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]


def test_merge_sort_reverse_sorted():
    arr = [5, 4, 3, 2, 1]
    translate.merge_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]


