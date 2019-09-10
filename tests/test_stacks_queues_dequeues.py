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


@pytest.mark.parametrize("original_list", [
    ([1,2,3]),
    (["hi", 2, "blah", 100])
])
def test_queue(original_list):
    queue = sqd.Queue(original_list)

    assert queue.size() == len(original_list)

    queue.enqueue("another item")
    assert queue.items[0] == "another item"

    last_item = original_list[-1]
    removed_item = queue.dequeue()
    assert removed_item == last_item
