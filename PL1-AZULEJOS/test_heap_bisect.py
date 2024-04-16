import pytest
from heap_bisect import HeapBis


def test_push():
    h = HeapBis([])
    h.push(3, "apple")
    assert h.peek() == (3, "apple"), "Push failed to add the element properly."


def test_pop():
    h = HeapBis([(5, "banana"), (1, "orange")])
    assert h.pop() == (5, "banana"), "Pop did not return the largest element."
    assert h.pop() == (1, "orange"), "Pop did not correctly pop the remaining element."
    with pytest.raises(Exception):
        h.pop()


def test_peek():
    h = HeapBis([(4, "melon"), (2, "kiwi")])
    assert h.peek() == (4, "melon"), "Peek did not return the max element."
    with pytest.raises(Exception):
        h_empty = HeapBis([])
        h_empty.peek()


def test_pop_max_below():
    h = HeapBis([(7, "grapes"), (5, "pear"), (6, "peach")])
    assert h.pop_max_below(6) == (
        5,
        "pear",
    ), "pop_max_below did not return correct element."
    assert h.pop_max_below(3) is None, "pop_max_below isn't None."


def test_pop_min_above():
    h = HeapBis([(7, "grapes"), (5, "pear"), (6, "peach")])
    assert h.pop_min_above(5) == (
        6,
        "peach",
    ), "pop_min_above did not return correct element."


def test_len():
    h = HeapBis([(1, "strawberry"), (2, "raspberry")])
    assert len(h) == 2, "Length did not match the number of elements."


def test_str():
    h = HeapBis([(2, "cherry")])
    assert (
        str(h) == "[(-2, 'cherry')]"
    ), "String representation of the heap is incorrect."