import pytest
from unittest.mock import AsyncMock
from starlette.requests import Request
from tortoise.queryset import QuerySet
from fastapi_admin.widgets.filters import (
    Filter, Search, Datetime, Date, Select, Enum, ForeignKey, DistinctColumn, Boolean
)
from enum import Enum as EnumCLS


@pytest.mark.asyncio
async def test_filter_init():
    f = Filter(name="test", label="Test")
    assert f.context["name"] == "test"
    assert f.context["label"] == "Test"


@pytest.mark.asyncio
async def test_filter_get_queryset():
    f = Filter(name="test", label="Test")
    request = AsyncMock(Request)
    qs = AsyncMock(QuerySet)
    await f.get_queryset(request, "value", qs)
    qs.filter.assert_called_with(test="value")


@pytest.mark.asyncio
async def test_search_init():
    s = Search(name="test", label="Test", search_mode="contains")
    assert s.context["name"] == "test__contains"


@pytest.mark.asyncio
async def test_datetime_init():
    dt = Datetime(name="test", label="Test")
    assert dt.context["name"] == "test__range"


@pytest.mark.asyncio
async def test_date_init():
    d = Date(name="test", label="Test")
    assert d.context["name"] == "test__range"


@pytest.mark.asyncio
async def test_select_init():
    s = Select(name="test", label="Test")
    assert s.context["name"] == "test"


@pytest.mark.asyncio
async def test_enum_init():
    class TempEnum(EnumCLS):
        VALUE1 = 1
        VALUE2 = 2

    e = Enum(enum=TempEnum, name="test", label="Test")
    assert e.enum == TempEnum
    assert e.context["name"] == "test"


@pytest.mark.asyncio
async def test_foreignkey_init():
    fk = ForeignKey(model=AsyncMock(), name="test", label="Test")
    assert fk.context["name"] == "test"


@pytest.mark.asyncio
async def test_distinctcolumn_init():
    dc = DistinctColumn(model=AsyncMock(), name="test", label="Test")
    assert dc.context["name"] == "test"


@pytest.mark.asyncio
async def test_boolean_get_options():
    b = Boolean(name="test", label="Test")
    options = await b.get_options()
    assert options == [("", ""), ("TRUE", "true"), ("FALSE", "false")]


@pytest.mark.asyncio
async def test_boolean_get_queryset():
    b = Boolean(name="test", label="Test")
    request = AsyncMock(Request)
    qs = AsyncMock(QuerySet)
    await b.get_queryset(request, "true", qs)
    qs.filter.assert_called_with(test=True)
    await b.get_queryset(request, "false", qs)
    qs.filter.assert_called_with(test=False)
