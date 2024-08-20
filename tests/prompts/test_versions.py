# This file was auto-generated by Fern from our API Definition.

import typing

from label_studio_sdk.client import AsyncLabelStudio, LabelStudio

from ..utilities import validate_response


async def test_create(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "title": "title",
        "parent_model": 1,
        "prompt": "prompt",
        "provider": "OpenAI",
        "provider_model_id": "provider_model_id",
        "created_by": 1,
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "organization": 1,
    }
    expected_types: typing.Any = {
        "title": None,
        "parent_model": "integer",
        "prompt": None,
        "provider": None,
        "provider_model_id": None,
        "created_by": "integer",
        "created_at": "datetime",
        "updated_at": "datetime",
        "organization": "integer",
    }
    response = client.prompts.versions.create(
        id=1, title="title", prompt="prompt", provider="OpenAI", provider_model_id="provider_model_id"
    )
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.prompts.versions.create(
        id=1, title="title", prompt="prompt", provider="OpenAI", provider_model_id="provider_model_id"
    )
    validate_response(async_response, expected_response, expected_types)


async def test_create_run(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "organization": 1,
        "project": 1,
        "model_version": "model_version",
        "created_by": 1,
        "project_subset": "All",
        "status": "Pending",
        "job_id": "job_id",
        "total_predictions": 1,
        "total_correct_predictions": 1,
        "total_tasks": 1,
        "created_at": "2024-01-15T09:30:00Z",
        "triggered_at": "2024-01-15T09:30:00Z",
        "predictions_updated_at": "2024-01-15T09:30:00Z",
        "completed_at": "2024-01-15T09:30:00Z",
    }
    expected_types: typing.Any = {
        "organization": "integer",
        "project": "integer",
        "model_version": None,
        "created_by": "integer",
        "project_subset": None,
        "status": None,
        "job_id": None,
        "total_predictions": "integer",
        "total_correct_predictions": "integer",
        "total_tasks": "integer",
        "created_at": "datetime",
        "triggered_at": "datetime",
        "predictions_updated_at": "datetime",
        "completed_at": "datetime",
    }
    response = client.prompts.versions.create_run(id=1, version_id=1, project=1, project_subset="All")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.prompts.versions.create_run(id=1, version_id=1, project=1, project_subset="All")
    validate_response(async_response, expected_response, expected_types)
