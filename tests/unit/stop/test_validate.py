from src.stop.validate import validate_stop
from tests.unit.test_classes import TestMessage, TestAuthor, TestRole

top_role = TestRole()
author = TestAuthor()
author.top_role = top_role
test_command = TestMessage
test_command.author = author


def test_validate_stop():
    """ Check that validating ping commands works as expected when given valid input """
    test_command.author.top_role.name = "Landlord"

    assert validate_stop(test_command) is True


def test_validate_ping_guest_role():
    """ Check that validating ping commands works as expected when given invalid input """
    test_command.author.top_role.name = "Guest"

    assert validate_stop(test_command) is False

    test_command.author.top_role.name = "Manager"

    assert validate_stop(test_command) is False

    test_command.author.top_role.name = "Admin"

    assert validate_stop(test_command) is False
