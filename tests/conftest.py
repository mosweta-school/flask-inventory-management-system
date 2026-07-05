import pytest
from app import app
from inventory.database import inventory


@pytest.fixture(autouse=True)
def clear_inventory():
    inventory.clear()
    yield
    inventory.clear()


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client