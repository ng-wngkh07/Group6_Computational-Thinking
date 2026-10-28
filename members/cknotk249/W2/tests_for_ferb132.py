import pytest

from members.ferb132.W1.grades import summary
from members.ferb132.W1.rules import can_register_thesis, missing
from members.ferb132.W1.text_tools import top_k, word_count
from members.ferb132.W1.timetable import by_day
from members.ferb132.W1.translate import binary_to_demical



# 1. Tests cho translate.py (binary_to_demical)

def test_binary_to_demical_standard():
    """Kiểm tra chuyển đổi chuỗi nhị phân thông thường sang thập phân."""
    assert binary_to_demical("1100") == 12
    assert binary_to_demical("1010") == 10
    assert binary_to_demical("11111111") == 255


def test_binary_to_demical_edge_empty_and_leading_zeros():
    """Edge case: Chuỗi rỗng, chuỗi toàn số 0 và chuỗi có nhiều số 0 ở đầu."""
    assert binary_to_demical("") == 0
    assert binary_to_demical("0000") == 0
    assert binary_to_demical("0000101") == 5



# 2. Tests cho timetable.py (by_day)

def test_by_day_groups_and_sorts_courses():
    """Kiểm tra nhóm môn học theo ngày và tự động sắp xếp theo thứ tự bảng chữ cái."""
    schedule = [
        ("CSC10014", "Mon"),
        ("MTH00003", "Tue"),
        ("CSC10001", "Mon"),
        ("PHY00001", "Tue"),
    ]
    expected = {
        "Mon": ["CSC10001", "CSC10014"],
        "Tue": ["MTH00003", "PHY00001"],
    }
    assert by_day(schedule) == expected


def test_by_day_edge_empty_schedule():
    """Edge case: Lịch học rỗng phải trả về dictionary rỗng."""
    assert by_day([]) == {}



# 3. Tests cho text_tools.py (word_count & top_k)

def test_word_count_ignores_case_and_punctuation():
    """Kiểm tra đếm từ không phân biệt hoa thường và loại bỏ dấu câu .,!?;:."""
    text = "Git is fun. git IS fast! Fun, fun; fast?"
    assert word_count(text) == {"git": 2, "is": 2, "fun": 3, "fast": 2}


def test_top_k_tie_breaking_alphabetical():
    """Edge case: Khi các từ có cùng số lần xuất hiện, top_k sắp xếp theo thứ tự từ điển."""
    text = "banana apple cherry banana apple cherry"
    # Cả 3 từ đều xuất hiện 2 lần -> ưu tiên 'apple' rồi đến 'banana'
    assert top_k(text, 2) == [("apple", 2), ("banana", 2)]


def test_text_tools_edge_only_punctuation_and_zero_k():
    """Edge case: Chuỗi chỉ chứa dấu câu/khoảng trắng hoặc k = 0."""
    assert word_count("... !!! ??? ; : ,") == {}
    assert top_k("... !!! ???", 3) == []
    assert top_k("Python is great", 0) == []



# 4. Tests cho grades.py (summary)

def test_summary_even_and_odd_lengths():
    """Kiểm tra tính max, min, mean, median với danh sách chẵn và lẻ phần tử."""
    even_res = summary([7.5, 9.0, 6.0, 8.0])
    assert even_res == {"max": 9.0, "min": 6.0, "mean": 7.62, "median": 7.75}

    odd_res = summary([10.0, 5.0, 8.0])
    assert odd_res == {"max": 10.0, "min": 5.0, "mean": 7.67, "median": 8.0}


def test_summary_edge_single_element_and_negative_float():
    """Edge case: Danh sách chỉ có đúng 1 điểm số."""
    single_res = summary([8.25])
    assert single_res == {"max": 8.25, "min": 8.25, "mean": 8.25, "median": 8.25}


def test_summary_edge_empty_list_raises_value_error():
    """Edge case: Danh sách điểm rỗng phải quăng ngoại lệ ValueError."""
    with pytest.raises(ValueError):
        summary([])



# 5. Tests cho rules.py (can_register_thesis & missing)

def test_can_register_thesis_boundary_values():
    """Edge case: Kiểm tra giá trị nằm ngay tại biên (credits = 120, gpa = 2.0)."""
    assert can_register_thesis(120, 2.0) is True
    assert can_register_thesis(119, 2.0) is False
    assert can_register_thesis(120, 1.99) is False
    assert missing(120, 2.0) == []


def test_missing_singular_vs_plural_credits_and_gpa():
    """Edge case: Kiểm tra cách chia danh từ số ít ('1 more credit') và số nhiều ('credits')."""
    assert missing(119, 2.5) == ["need 1 more credit"]
    assert missing(118, 1.5) == ["need 2 more credits", "need 0.5 more GPA"]