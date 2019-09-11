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


@pytest.mark.parametrize("my_stack", [
    (sqd.Stack([1,2,3])),
    (sqd.Stack(["hi", 2, "blah", 100]))
])
def test_queue_enqueue(my_stack):
    queue = sqd.Queue(my_stack)

    assert queue.size() == len(my_stack.items)

    queue.enqueue("another item")
    assert queue.stack.items[0] == "another item"
