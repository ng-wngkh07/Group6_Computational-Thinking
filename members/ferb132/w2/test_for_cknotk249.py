import pytest
# Thay "teammate_name" bằng tên thư mục của đồng đội bạn
from members.cknotk249.W1.grades import summary 

# 1. Test case thông thường (theo ví dụ của đề bài)
def test_summary_normal_case():
    result = summary([7.5, 9, 6, 8])
    assert result == {'min': 6, 'max': 9, 'mean': 7.62, 'median': 7.75}

# 2. Test case khi mảng chỉ có 1 phần tử
def test_summary_single_element():
    result = summary([8.5])
    assert result == {'min': 8.5, 'max': 8.5, 'mean': 8.5, 'median': 8.5}

# 3. Test case khi có điểm âm (mặc dù thực tế điểm ít khi âm, nhưng hàm vẫn phải tính đúng toán học)
def test_summary_negative_scores():
    result = summary([-2, 0, 4])
    assert result == {'min': -2, 'max': 4, 'mean': 0.67, 'median': 0.0}

# 4. Test case kiểm tra xử lý lỗi khi list rỗng (Exception)
def test_summary_empty_list():
    with pytest.raises(ValueError):
        summary([])

# 5. EDGE CASE (Trường hợp đặc biệt): Đầu vào là các số thực dài vô tận
# Để kiểm tra xem đồng đội có thực sự dùng hàm round(..., 2) cho mean và median như đề bài yêu cầu không.
def test_summary_edge_case_precision():
    # Trung bình của [1.111, 2.222, 3.333] là 2.222.
    # Median cũng là 2.222. 
    # Nếu code đúng, nó phải làm tròn thành 2.22.
    result = summary([1.111, 2.222, 3.333])
    
    assert result['mean'] == 2.22
    assert result['median'] == 2.22
    assert result['min'] == 1.111
    assert result['max'] == 3.333