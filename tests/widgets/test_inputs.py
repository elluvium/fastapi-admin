import pytest
from starlette.requests import Request
from fastapi_admin.widgets.inputs import (
    Input, DisplayOnly, Text, Select, ForeignKey, ManyToMany, Enum, Email, Json, TextArea, Editor, DateTime, Date, File,
    Image, Radio, RadioEnum, Switch, Password, Number, Color
)
from tortoise import Model
from enum import Enum as EnumCLS
from fastapi_admin.file_upload import FileUpload
from starlette.datastructures import UploadFile


class TestModel(Model):
    pass


@pytest.mark.asyncio
async def test_display_only():
    widget = DisplayOnly()
    assert isinstance(widget, DisplayOnly)