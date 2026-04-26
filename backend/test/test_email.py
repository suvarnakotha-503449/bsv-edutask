import pytest
from unittest.mock import MagicMock
from src.controllers.usercontroller import UserController

def test_get_user_by_email_success():
    # Setup mock DAO
    mock_dao = MagicMock()
    mock_user = {"email": "valid@student.bth.se", "name": "Student"}
    

    mock_dao.find.return_value = [mock_user] 
    controller = UserController(dao=mock_dao)
    
    result = controller.get_user_by_email("valid@student.bth.se")
    assert result == mock_user

def test_get_user_by_email_not_found():
    mock_dao = MagicMock()
    mock_dao.find.return_value = [] 
    
    controller = UserController(dao=mock_dao)
    result = controller.get_user_by_email("unregistered@student.bth.se")
    assert result is None

def test_get_user_by_email_multiple_users():
    mock_dao = MagicMock()
    mock_user1 = {"email": "Ruthik@student.bth.se", "name": "user1"}
    mock_user2 = {"email": "Suvarna@student.bth.se", "name": "user2"}
    mock_dao.find.return_value = [mock_user1, mock_user2]
    
    controller = UserController(dao=mock_dao)
    result = controller.get_user_by_email("duplicate@student.bth.se")
    
    assert result == mock_user1

def test_get_user_by_email_invalid_format():
    mock_dao = MagicMock()
    controller = UserController(dao=mock_dao)
    with pytest.raises(ValueError):
        controller.get_user_by_email("invalid-email-format")
