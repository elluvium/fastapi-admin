import pytest
from starlette.requests import Request
from starlette.datastructures import UploadFile
from tortoise import Model
from fastapi_admin.widgets.inputs import Input, DisplayOnly, Text, Select, ForeignKey, ManyToMany, Enum, Email, Json, TextArea, Editor, DateTime, Date, File, Image, Radio, RadioEnum, Switch, Password, Number, Color
from fastapi_admin.file_upload import FileUpload

@pytest.mark.asyncio
async def test_input_render():
    input_widget = Input()
    request = Request(scope={"type": "http"})
    result = await input_widget.render(request, None)
    assert result is not None

@pytest.mark.asyncio
async def test_text_render():
    text_widget = Text()
    request = Request(scope={"type": "http"})
    result = await text_widget.render(request, None)
    assert result is not None

@pytest.mark.asyncio
async def test_email_render():
    email_widget = Email()
    request = Request(scope={"type": "http"})
    result = await email_widget.render(request, None)
    assert result is not None

@pytest.mark.asyncio
async def test_json_render():
    json_widget = Json()
    request = Request(scope={"type": "http"})
    result = await json_widget.render(request, None)
    assert result is not None

@pytest.mark.asyncio
async def test_text_area_render():
    text_area_widget = TextArea()
    request = Request(scope={"type": "http"})
    result = await text_area_widget.render(request, None)
    assert result is not None

@pytest.mark.asyncio
async def test_editor_render():
    editor_widget = Editor()
    request = Request(scope={"type": "http"})
    result = await editor_widget.render(request, None)
    assert result is not None

@pytest.mark.asyncio
async def test_date_time_render():
    date_time_widget = DateTime()
    request = Request(scope={"type": "http"})
    result = await date_time_widget.render(request, None)
    assert result is not None

@pytest.mark.asyncio
async def test_date_render():
    date_widget = Date()
    request = Request(scope={"type": "http"})
    result = await date_widget.render(request, None)
    assert result is not None

@pytest.mark.asyncio
async def test_file_render():
    file_upload = FileUpload(uploads_dir="/tmp")
    file_widget = File(upload=file_upload)
    request = Request(scope={"type": "http"})
    result = await file_widget.render(request, None)
    assert result is not None

@pytest.mark.asyncio
async def test_image_render():
    file_upload = FileUpload(uploads_dir="/tmp")
    image_widget = Image(upload=file_upload)
    request = Request(scope={"type": "http"})
    result = await image_widget.render(request, None)
    assert result is not None

@pytest.mark.asyncio
async def test_radio_render():
    radio_widget = Radio(options=[("Option1", "1"), ("Option2", "2")])
    request = Request(scope={"type": "http"})
    result = await radio_widget.render(request, None)
    assert result is not None

@pytest.mark.asyncio
async def test_switch_render():
    switch_widget = Switch()
    request = Request(scope={"type": "http"})
    result = await switch_widget.render(request, None)
    assert result is not None

@pytest.mark.asyncio
async def test_password_render():
    password_widget = Password()
    request = Request(scope={"type": "http"})
    result = await password_widget.render(request, None)
    assert result is not None

@pytest.mark.asyncio
async def test_number_render():
    number_widget = Number()
    request = Request(scope={"type": "http"})
    result = await number_widget.render(request, None)
    assert result is not None

@pytest.mark.asyncio
async def test_color_render():
    color_widget = Color()
    request = Request(scope={"type": "http"})
    result = await color_widget.render(request, None)
    assert result is not None