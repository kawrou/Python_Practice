from lib.user import User

"""
test posts are constructed with a title, content, views, and user_id
"""

def test_user_construct():
    user1 = User(1,'aisha@hotmail.com', 'aisha')
    assert user1.id == 1
    assert user1.email_address == 'aisha@hotmail.com'
    assert user1.username == 'aisha'