import pytest
import algos.stacks_queues_dequeues as sqd


@pytest.mark.parametrize("original_list, expected", [
    ([1,2,3], [3,2,1]),
    ([1,1], [1,1]),
    (["hi", "bye", "wahoo"], ["wahoo", "bye", "hi"])
])
def test_reversed_list(original_list, expected):
    actual = sqd.reversed_list(original_list)
    assert actual == expected
