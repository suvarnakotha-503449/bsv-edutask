import pytest
from unittest.mock import MagicMock

# Notice we are importing the CLASS here, not the function!
from src.controllers.usercontroller import UserController 

def test_get_user_by_email_success():
    mock_dao = MagicMock()
    mock_user = {"email": "valid@student.bth.se", "name": "Test Student"}
    
    mock_dao.find.return_value = [mock_user]
    mock_dao.findOne.return_value = mock_user
    
    controller = UserController(dao=mock_dao)
    result = controller.get_user_by_email("valid@student.bth.se")
    assert result == mock_user

def test_get_user_by_email_not_found():
    mock_dao = MagicMock()
    mock_dao.find.return_value = []
    mock_dao.findOne.return_value = None
    
    controller = UserController(dao=mock_dao)
    result = controller.get_user_by_email("unregistered@student.bth.se")
    assert result is None

def test_get_user_by_email_invalid_format():
    mock_dao = MagicMock()
    controller = UserController(dao=mock_dao)
    
    result = controller.get_user_by_email("invalid-email-format")
    assert result is None