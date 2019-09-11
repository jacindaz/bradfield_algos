import pytest
from algos.stacks_queues_dequeues import Stack, reversed_list, Queue


@pytest.mark.parametrize("original_list, expected", [
    (Stack([1,2,3]), [3,2,1]),
    (Stack([1,1]), [1,1]),
    (Stack(["hi", "bye", "wahoo"]), ["wahoo", "bye", "hi"])
])
def test_reversed_list(original_list, expected):
    actual = reversed_list(original_list)
    assert actual == expected


@pytest.mark.parametrize("my_stack", [
    (Stack([1,2,3])),
    (Stack(["hi", 2, "blah", 100]))
])
def test_queue_enqueue(my_stack):
    queue = Queue(my_stack)

    assert queue.size() == len(my_stack.items)

    queue.enqueue("another item")
    assert queue.stack.items[0] == "another item"


@pytest.mark.parametrize("my_stack, expected_size, expected_is_empty", [
    (Stack([1,2,3]), 3, False),
    (Stack(["hi", 2, "blah", 100]), 4, False),
    (Stack([]), 0, True)
])
def test_queue_dequeue(my_stack, expected_size, expected_is_empty):
    queue = Queue(my_stack)

    assert queue.size() == expected_size
    assert queue.is_empty() == expected_is_empty

    if not queue.is_empty():
        last_item = my_stack.items[-1]
        removed_item = queue.dequeue()
        assert removed_item == last_item
