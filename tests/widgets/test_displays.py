import pytest
from starlette.requests import Request
from datetime import datetime
from fastapi_admin.widgets.displays import DatetimeDisplay, DateDisplay, Boolean, Image

@pytest.fixture
async def mock_request():
    return Request(scope={"type": "http"})

# Passed test cases

def test_datetime_display_init():
    display = DatetimeDisplay()
    assert display.format_ == "%Y-%m-%d %H:%M:%S"

def test_boolean_template():
    display = Boolean()
    assert display.template == "widgets/displays/boolean.html"

def test_image_template():
    display = Image()
    assert display.template == "widgets/displays/image.html"

def test_image_init():
    display = Image(width="100px", height="100px")
    assert display.context["width"] == "100px"
    assert display.context["height"] == "100px"
