import pytest
from starlette.requests import Request
from fastapi_admin.widgets.inputs import (
    Input, DisplayOnly, Text, Select, ForeignKey, ManyToMany, Enum, Email,
    Json, TextArea, Editor, DateTime, Date, File, Image, Radio, RadioEnum,
    Switch, Password, Number, Color
)


@pytest.mark.asyncio
async def test_input_initialization():
    input_widget = Input(help_text='Test Help', default='Default Value', null=True)
    assert input_widget.context['help_text'] == 'Test Help'
    assert input_widget.default == 'Default Value'
    assert input_widget.context['null'] is True


@pytest.mark.asyncio
async def test_input_parse_value():
    request = Request({
        "type": "http",
        "method": "GET",
        "path": "/",
        "headers": [],
    })
    input_widget = Input()
    value = await input_widget.parse_value(request, 'test')
    assert value == 'test'


@pytest.mark.asyncio
async def test_input_render():
    request = Request({
        "type": "http",
        "method": "GET",
        "path": "/",
        "headers": [],
    })
    input_widget = Input(default='Default Value')
    rendered_value = await input_widget.render(request, None)
    assert 'Default Value' in rendered_value
