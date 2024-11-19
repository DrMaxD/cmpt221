import pytest

from sqlalchemy import insert, select, text
from models import User

# test db connection
def test_db_connection(db_session):
    # Use db_session to interact with the database
    result = db_session.execute(text("SELECT 1"))
    assert result.scalar() == 1

# test to insert a user
# you can count this as one of your 5 test cases :)
def test_insert_user(db_session, sample_signup_input):
    insert_stmt = insert(User).values(sample_signup_input)

    # execute insert query
    db_session.execute(insert_stmt)
    # commit the changes to the db
    db_session.commit()

    # not part of the app.py code, just being used to get the inserted data
    selected_user = db_session.query(User).filter_by(FirstName="Calista").first()

    assert selected_user is not None
    assert selected_user.LastName == "Phippen"

# test to update a user
def test_update_user(db_session, sample_signup_input):
    # First, insert a user
    insert_stmt = insert(User).values(sample_signup_input)
    db_session.execute(insert_stmt)
    db_session.commit()

    # Verify the user is inserted
    selected_user = db_session.query(User).filter_by(Email=sample_signup_input['Email']).first()
    assert selected_user is not None

    # Update user's first name
    selected_user.FirstName = "UpdatedName"
    db_session.commit()

    # Verify the user's first name is updated
    updated_user = db_session.query(User).filter_by(Email=sample_signup_input['Email']).first()
    assert updated_user.FirstName == "UpdatedName"

# test updating a non-existent user
def test_update_nonexistent_user(db_session):
    # Attempt to update a user that does not exist
    non_existent_user_email = "nonexistent@marist.edu"
    update_stmt = db_session.query(User).filter_by(Email=non_existent_user_email).update({"FirstName": "ShouldNotUpdate"})
    db_session.commit()

    # Verify the user does not exist
    updated_user = db_session.query(User).filter_by(Email=non_existent_user_email).first()
    assert updated_user is None


def test_insert_user_missing_primary_key(db_session, sample_signup_input):
  # Set "UserID" to None to simulate missing primary key
  sample_signup_input["UserID"] = None

  # Attempt to insert the user
  insert_stmt = insert(User).values(sample_signup_input)
  with pytest.raises(Exception) as excinfo:
    db_session.execute(insert_stmt)
    db_session.commit()

  # Assert on the error message (adjusted for your specific database)
  assert "null value in column" in str(excinfo.value)




