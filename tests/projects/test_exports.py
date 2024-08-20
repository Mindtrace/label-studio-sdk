# This file was auto-generated by Fern from our API Definition.

import typing

from label_studio_sdk.client import AsyncLabelStudio, LabelStudio

from ..utilities import validate_response


async def test_list_formats(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = ["string"]
    expected_types: typing.Any = ("list", {0: None})
    response = client.projects.exports.list_formats(id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.projects.exports.list_formats(id=1)
    validate_response(async_response, expected_response, expected_types)


async def test_list_(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = [
        {
            "title": "title",
            "id": 1,
            "created_by": {
                "id": 1,
                "first_name": "first_name",
                "last_name": "last_name",
                "email": "email",
                "avatar": "avatar",
            },
            "created_at": "2024-01-15T09:30:00Z",
            "finished_at": "2024-01-15T09:30:00Z",
            "status": "created",
            "md5": "md5",
            "counters": {"key": "value"},
            "converted_formats": [{"export_type": "export_type"}],
        }
    ]
    expected_types: typing.Any = (
        "list",
        {
            0: {
                "title": None,
                "id": "integer",
                "created_by": {"id": "integer", "first_name": None, "last_name": None, "email": None, "avatar": None},
                "created_at": "datetime",
                "finished_at": "datetime",
                "status": None,
                "md5": None,
                "counters": ("dict", {0: (None, None)}),
                "converted_formats": ("list", {0: {"export_type": None}}),
            }
        },
    )
    response = client.projects.exports.list(id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.projects.exports.list(id=1)
    validate_response(async_response, expected_response, expected_types)


async def test_create(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "title": "title",
        "id": 1,
        "created_by": {
            "id": 1,
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email",
            "avatar": "avatar",
        },
        "created_at": "2024-01-15T09:30:00Z",
        "finished_at": "2024-01-15T09:30:00Z",
        "status": "created",
        "md5": "md5",
        "counters": {"key": "value"},
        "converted_formats": [{"id": 1, "status": "created", "export_type": "export_type", "traceback": "traceback"}],
        "task_filter_options": {
            "view": 1,
            "skipped": "skipped",
            "finished": "finished",
            "annotated": "annotated",
            "only_with_annotations": True,
        },
        "annotation_filter_options": {"usual": True, "ground_truth": True, "skipped": True},
        "serialization_options": {
            "drafts": {"only_id": True},
            "predictions": {"only_id": True},
            "include_annotation_history": True,
            "annotations__completed_by": {"only_id": True},
            "interpolate_key_frames": True,
        },
    }
    expected_types: typing.Any = {
        "title": None,
        "id": "integer",
        "created_by": {"id": "integer", "first_name": None, "last_name": None, "email": None, "avatar": None},
        "created_at": "datetime",
        "finished_at": "datetime",
        "status": None,
        "md5": None,
        "counters": ("dict", {0: (None, None)}),
        "converted_formats": ("list", {0: {"id": "integer", "status": None, "export_type": None, "traceback": None}}),
        "task_filter_options": {
            "view": "integer",
            "skipped": None,
            "finished": None,
            "annotated": None,
            "only_with_annotations": None,
        },
        "annotation_filter_options": {"usual": None, "ground_truth": None, "skipped": None},
        "serialization_options": {
            "drafts": {"only_id": None},
            "predictions": {"only_id": None},
            "include_annotation_history": None,
            "annotations__completed_by": {"only_id": None},
            "interpolate_key_frames": None,
        },
    }
    response = client.projects.exports.create(id_=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.projects.exports.create(id_=1)
    validate_response(async_response, expected_response, expected_types)


async def test_get(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "title": "title",
        "id": 1,
        "created_by": {
            "id": 1,
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email",
            "avatar": "avatar",
        },
        "created_at": "2024-01-15T09:30:00Z",
        "finished_at": "2024-01-15T09:30:00Z",
        "status": "created",
        "md5": "md5",
        "counters": {"key": "value"},
        "converted_formats": [{"id": 1, "status": "created", "export_type": "export_type", "traceback": "traceback"}],
    }
    expected_types: typing.Any = {
        "title": None,
        "id": "integer",
        "created_by": {"id": "integer", "first_name": None, "last_name": None, "email": None, "avatar": None},
        "created_at": "datetime",
        "finished_at": "datetime",
        "status": None,
        "md5": None,
        "counters": ("dict", {0: (None, None)}),
        "converted_formats": ("list", {0: {"id": "integer", "status": None, "export_type": None, "traceback": None}}),
    }
    response = client.projects.exports.get(id=1, export_pk="export_pk")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.projects.exports.get(id=1, export_pk="export_pk")
    validate_response(async_response, expected_response, expected_types)


async def test_delete(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.projects.exports.delete(id=1, export_pk="export_pk") is None  # type: ignore[func-returns-value]

    assert await async_client.projects.exports.delete(id=1, export_pk="export_pk") is None  # type: ignore[func-returns-value]


async def test_convert(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {"export_type": "export_type"}
    expected_types: typing.Any = {"export_type": None}
    response = client.projects.exports.convert(id=1, export_pk="export_pk", export_type="export_type")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.projects.exports.convert(id=1, export_pk="export_pk", export_type="export_type")
    validate_response(async_response, expected_response, expected_types)


async def test_download(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.projects.exports.download(id=1, export_pk="export_pk") is None  # type: ignore[func-returns-value]

    assert await async_client.projects.exports.download(id=1, export_pk="export_pk") is None  # type: ignore[func-returns-value]
