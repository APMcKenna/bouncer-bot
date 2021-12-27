from src.ping.validate import validate_ping
from tests.unit.test_classes import TestMessage, TestAuthor, TestRole

top_role = TestRole()
author = TestAuthor()
author.top_role = top_role
test_command = TestMessage
test_command.author = author


def test_validate_ping():
    """ Check that validating ping commands works as expected when given valid input """
    test_command.author.top_role.name = "Landlord"

    assert validate_ping(test_command) is True

    test_command.author.top_role.name = "Manager"

    assert validate_ping(test_command) is True

    test_command.author.top_role.name = "Admin"

    assert validate_ping(test_command) is True


def test_validate_ping_guest_role():
    """ Check that validating ping commands works as expected when given invalid input """
    test_command.author.top_role.name = "Guest"

    assert validate_ping(test_command) is False
