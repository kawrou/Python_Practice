from lib.post import *
from lib.users_repository import *

def test_get_all_users(db_connection): 
    """
    returns a list of all user instances
    """
    db_connection.seed("seeds/social_network.sql")
    repository = Users_repository(db_connection)

    users = repository.all()

    assert users == [
        User(1, 'aisha@hotmail.com', 'aisha'),
        User(2, 'john.doe@example.com', 'john_doe'),
        User(3, 'emma.smith@gmail.com', 'emma_smith'),
        User(4, 'michael.jones@yahoo.com', 'michael_jones'),
        User(5, 'laura.miller@hotmail.com', 'laura_miller'),
        User(6, 'kevin.white@gmail.com', 'kevin_white'),
        User(7, 'natalie.brown@yahoo.com', 'natalie_brown'),
        User(8, 'peter.clark@example.com', 'peter_clark'),
        User(9, 'olivia.wilson@hotmail.com', 'olivia_wilson'),
        User(10, 'sam.carter@gmail.com', 'sam_carter'), 
    ]

def test_find_user_by_id(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = Users_repository(db_connection)

    users = repository.find(2)

    assert users == User(2, 'john.doe@example.com', 'john_doe')

def test_create_new_user(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = Users_repository(db_connection)

    new_user = repository.create('alan@hotmail.com', 'Alan')
    
    assert repository.find(11) == User(11, 'alan@hotmail.com', 'Alan')

def test_delete_new_user(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = Users_repository(db_connection)

    new_user = repository.create('alan@hotmail.com', 'Alan')
    assert repository.find(11) == User(11, 'alan@hotmail.com', 'Alan')
    
    repository.delete(11)
    
    all_users = repository.all()
    assert all_users == [
        User(1, 'aisha@hotmail.com', 'aisha'),
        User(2, 'john.doe@example.com', 'john_doe'),
        User(3, 'emma.smith@gmail.com', 'emma_smith'),
        User(4, 'michael.jones@yahoo.com', 'michael_jones'),
        User(5, 'laura.miller@hotmail.com', 'laura_miller'),
        User(6, 'kevin.white@gmail.com', 'kevin_white'),
        User(7, 'natalie.brown@yahoo.com', 'natalie_brown'),
        User(8, 'peter.clark@example.com', 'peter_clark'),
        User(9, 'olivia.wilson@hotmail.com', 'olivia_wilson'),
        User(10, 'sam.carter@gmail.com', 'sam_carter'),
    ]
    
