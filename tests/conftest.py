from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture
def client():
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def reset_activities():
    baseline = deepcopy(app_module.activities)

    # Ensure each test starts with a clean in-memory dataset.
    app_module.activities = deepcopy(baseline)
    yield
    app_module.activities = deepcopy(baseline)
