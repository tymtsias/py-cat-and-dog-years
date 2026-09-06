from app.main import get_human_age


def test_should_return_array_of_two_elements() -> None:
    assert len(get_human_age(15, 15)) == 2


def test_should_zero_values_if_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_values_if_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_values_if_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_values_if_more_than_15() -> None:
    assert get_human_age(16, 16) == [1, 1]


def test_should_return_values_if_23() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_values_with_big_age_more() -> None:
    assert get_human_age(100, 100) == [21, 17]
