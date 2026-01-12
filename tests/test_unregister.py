from src.app import activities, unregister_from_activity
from fastapi import HTTPException


def test_unregister_existing_participant():
    activity = 'Basketball'
    email = 'temp@test.edu'
    # add temp participant
    activities[activity]['participants'].append(email)

    resp = unregister_from_activity(activity, email)
    assert resp == {"message": f"Unregistered {email} from {activity}"}
    assert email not in activities[activity]['participants']


def test_unregister_missing_participant():
    activity = 'Basketball'
    email = 'doesnotexist@test.edu'
    try:
        unregister_from_activity(activity, email)
        assert False, "Expected HTTPException"
    except HTTPException as e:
        assert e.status_code == 404


def test_unregister_missing_activity():
    activity = 'NoSuchActivity'
    email = 'someone@test.edu'
    try:
        unregister_from_activity(activity, email)
        assert False, "Expected HTTPException"
    except HTTPException as e:
        assert e.status_code == 404
