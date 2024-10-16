from exercises.help import get_name


def test_name_func() -> None:
    assert get_name(n="Alyssa") == "Alyssa"
