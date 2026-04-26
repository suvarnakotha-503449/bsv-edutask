import pytest
import pymongo
from src.util.dao import DAO

@pytest.fixture
def sut():
    dao = DAO(collection_name="user")
    dao.collection.delete_many({}) 
    yield dao
    dao.collection.delete_many({})

def test_create_valid_document(sut):
    valid_data = {
        "firstName": "Ruthik", 
        "lastName": "Garapati", 
        "email": "ruthik@student.bth.se"
    }
    result = sut.create(valid_data)
    assert result is not None
    assert '_id' in result

def test_create_missing_required_field(sut):
    invalid_data = {"firstName": "Suvarna"} 
    with pytest.raises(pymongo.errors.WriteError):
        sut.create(invalid_data)

def test_create_invalid_data_type(sut):
    invalid_data = {
        "firstName": "Test", 
        "lastName": "User", 
        "email": 12345
    } 
    with pytest.raises(pymongo.errors.WriteError):
        sut.create(invalid_data)