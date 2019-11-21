"""
Unit tests for DatabaseOperation class
"""

import pytest
from mock import Mock
from app.db_manage import DatabaseOperation


@pytest.fixture
def database():
    return DatabaseOperation()


@pytest.fixture
def mock_db():
    return Mock(spec=DatabaseOperation)


def test_config_read(database):
    db_config = database.read_db_config()
    assert db_config == {'host': 'localhost', 'database': 'python_mysql', 'user': 'root', 'password': 'password'}


def test_update_record(database):
    database.update_record(2, 'Marek')
