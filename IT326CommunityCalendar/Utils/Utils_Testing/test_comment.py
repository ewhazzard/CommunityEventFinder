import pytest

from Utils.comment import Comment
from event import Event
import datetime


def test_comment_creation():
    testComment = Comment("Looking forward to the event!",
                          5425, datetime.date(2022, 12, 5), 19587)

    assert testComment.get_content() == "Looking forward to the event!"
    assert testComment.get_comment_id == 5425
    assert testComment.get_date == datetime.date(2022, 12, 5)
    assert testComment.get_user_id == 19587

# def test_comment_on_event_posting():
#     content = Comment.set_content("Looking forward to the event!")
#     comment_id = 50
#     comment_date = datetime.date(2022, 12, 5)
#     user_id = 800695759

#     newComment = Comment(content, comment_id, comment_date, user_id)
#     assert newComment.get_comment_id()
