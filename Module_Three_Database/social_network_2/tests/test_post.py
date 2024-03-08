from lib.post import Post

"""
test posts are constructed with a title, content, views, and user_id
"""

def test_post_construct():
    post_1 = Post(1, "I`m feeling great", "It`s been a great day", 500, 1)
    assert post_1.id == 1
    assert post_1.title == 'I`m feeling great'
    assert post_1.content == 'It`s been a great day'
    assert post_1.views == 500
    assert post_1.user_id == 1
