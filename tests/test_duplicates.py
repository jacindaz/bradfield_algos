import pytest
import algos.duplicates as dupes


@pytest.mark.parametrize("input, expected", [
    ([1,2,1], True),
    ([1,2,3], False)
])
def test_duplicates(input, expected):
    actual1 = dupes.have_duplicates_n_squared(input)
    actual2 = dupes.have_duplicates1(input)
    actual3 = dupes.have_duplicates2(input)
    actual4 = dupes.have_duplicates3(input)
    actual5 = dupes.have_duplicates_set(input)

    assert actual1 == expected
    assert actual2 == expected
    assert actual3 == expected
    assert actual4 == expected
    assert actual5 == expected
