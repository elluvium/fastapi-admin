import pytest
from unittest.mock import Mock, patch
from jinja2 import Environment, FileSystemLoader
from starlette.requests import Request

from fastapi_admin.template import set_global_env, add_template_folder, templates


@pytest.fixture
def mock_request() -> Request:
    mock = Mock(spec=Request)
    mock.scope = {"raw_path": b"/mocked_path"}
    mock.query_params = {}
    return mock


def test_set_global_env():
    name = "TEST_NAME"
    value = "TEST_VALUE"
    set_global_env(name, value)
    assert templates.env.globals[name] == value


def test_add_template_folder():
    folder_path = "/new/template/folder"
    add_template_folder(folder_path)
    assert templates.env.loader.searchpath[0] == folder_path
