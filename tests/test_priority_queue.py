import pytest
from algos.priority_queue import MinBinaryHeap


@pytest.mark.parametrize("binary_tree, expected_tree", [
    (
        [0,5,9,11,14,18,19,21,33,17,27],
        [0,9,14,11,17,18,19,21,33,27]
    ),
    (
        [0,1,5,10,8,7],
        [0,5,7,10,8]
    )
])
def test_delete_min(binary_tree, expected_tree):
    heap = MinBinaryHeap(binary_tree)
    heap.delete_min()

    assert heap.items == expected_tree
