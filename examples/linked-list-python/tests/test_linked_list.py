import pytest
from pedagog_pytest import (
    HIDDEN, Expect, ExtraCredit, Rubric, Score, item, number, rubric, rubric_item, solution_expect, visibility,
)

from linked_list import LinkedList


@rubric_item("append keeps insertion order", points=2, id="append")
@number(1)
def test_append_and_to_list(score: Score):
    items = LinkedList()
    for value in [3, 1, 4]:
        items.append(value)
    assert items.to_list() == [3, 1, 4]
    score.award()


@rubric_item("len counts elements", points=2, id="len")
@number(2)
def test_len(score: Score):
    items = LinkedList()
    assert len(items) == 0
    score.award(1, reason="empty list")
    items.append("x")
    items.append("y")
    assert len(items) == 2
    score.award(1, reason="two elements")


class PopFront(Rubric):
    returns_front: Score = item("returns values from the front", points=2)
    raises_when_empty: Score = item("raises IndexError when empty", points=1)
    reusable: Score = item("the list still works after being emptied", points=1)


@rubric(PopFront, id="pop-front", name="pop_front")
@number(3)
@visibility(output=HIDDEN)
def test_pop_front(scores: PopFront):
    items = LinkedList()
    items.append(1)
    items.append(2)
    with scores.returns_front.check(reason="returns 1, then 2"):
        assert items.pop_front() == 1
        assert items.pop_front() == 2
    with scores.raises_when_empty.check(reason="raises IndexError once empty"):
        with pytest.raises(IndexError):
            items.pop_front()
    with scores.reusable.check(reason="append and to_list work after emptying"):
        items.append(3)
        assert items.to_list() == [3]


@rubric_item("stretch goal: reverse()", points=1, id="reverse", extra_credit=ExtraCredit.ATTEMPTED_WORK)
@number(4)
@solution_expect(Expect.FAIL)
def test_reverse_stretch_goal(score: Score):
    """Counts toward the total only for students who attempt it; the reference
    solution doesn't."""
    items = LinkedList()
    items.append(1)
    items.append(2)
    if hasattr(items, "reverse"):
        score.attempt()
    items.reverse()
    assert items.to_list() == [2, 1]
    score.award(reason="reverses in place")


@rubric_item("handles a thousand elements", points=2, id="many")
@number(5)
def test_many_elements(score: Score):
    items = LinkedList()
    for value in range(1000):
        items.append(value)
    result = items.to_list()
    if result[:10] == list(range(10)):
        score.award(1, reason="first 10 elements correct")
    assert result == list(range(1000))
    score.award(reason="all 1000 elements correct")
