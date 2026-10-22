
from members.hoagpac.w1.translate import binary_search


def test_find_first_element():
    assert binary_search([1, 3, 5, 7, 9], 1) == 0


def test_find_last_element():
    assert binary_search([1, 3, 5, 7, 9], 9) == 4


def test_single_element_found():
    assert binary_search([42], 42) == 0


def test_single_element_not_found():
    assert binary_search([42], 10) == -1


def test_negative_numbers():
    assert binary_search([-9, -5, -2, 0, 4], -5) == 1


def test_duplicate_elements():
    numbers = [1, 2, 2, 2, 5]
    index = binary_search(numbers, 2)

    assert index != -1
    assert numbers[index] == 2
