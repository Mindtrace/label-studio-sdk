# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.request_options import RequestOptions
from ...types.inference_run import InferenceRun
from ...types.inference_run_created_by import InferenceRunCreatedBy
from ...types.inference_run_organization import InferenceRunOrganization
from ...types.inference_run_project_subset import InferenceRunProjectSubset
from ...types.inference_run_status import InferenceRunStatus
from ...types.prompt_version import PromptVersion
from ...types.prompt_version_created_by import PromptVersionCreatedBy
from ...types.prompt_version_organization import PromptVersionOrganization
from ...types.prompt_version_provider import PromptVersionProvider

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class VersionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self,
        id: int,
        *,
        title: str,
        prompt: str,
        provider: PromptVersionProvider,
        provider_model_id: str,
        parent_model: typing.Optional[int] = OMIT,
        created_by: typing.Optional[PromptVersionCreatedBy] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        organization: typing.Optional[PromptVersionOrganization] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PromptVersion:
        """
        Create a new version of a prompt.

        Parameters
        ----------
        id : int
            Prompt ID

        title : str

        prompt : str

        provider : PromptVersionProvider

        provider_model_id : str

        parent_model : typing.Optional[int]

        created_by : typing.Optional[PromptVersionCreatedBy]

        created_at : typing.Optional[dt.datetime]

        updated_at : typing.Optional[dt.datetime]

        organization : typing.Optional[PromptVersionOrganization]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PromptVersion


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.prompts.versions.create(
            id=1,
            title="title",
            prompt="prompt",
            provider="OpenAI",
            provider_model_id="provider_model_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/prompts/{jsonable_encoder(id)}/versions",
            method="POST",
            json={
                "title": title,
                "parent_model": parent_model,
                "prompt": prompt,
                "provider": provider,
                "provider_model_id": provider_model_id,
                "created_by": created_by,
                "created_at": created_at,
                "updated_at": updated_at,
                "organization": organization,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(PromptVersion, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_run(
        self,
        id: int,
        version_id: int,
        *,
        project: int,
        project_subset: InferenceRunProjectSubset,
        organization: typing.Optional[InferenceRunOrganization] = OMIT,
        model_version: typing.Optional[str] = OMIT,
        created_by: typing.Optional[InferenceRunCreatedBy] = OMIT,
        status: typing.Optional[InferenceRunStatus] = OMIT,
        job_id: typing.Optional[str] = OMIT,
        total_predictions: typing.Optional[int] = OMIT,
        total_correct_predictions: typing.Optional[int] = OMIT,
        total_tasks: typing.Optional[int] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        triggered_at: typing.Optional[dt.datetime] = OMIT,
        predictions_updated_at: typing.Optional[dt.datetime] = OMIT,
        completed_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InferenceRun:
        """
        Run a prompt inference.

        Parameters
        ----------
        id : int
            Prompt ID

        version_id : int
            Prompt Version ID

        project : int

        project_subset : InferenceRunProjectSubset

        organization : typing.Optional[InferenceRunOrganization]

        model_version : typing.Optional[str]

        created_by : typing.Optional[InferenceRunCreatedBy]

        status : typing.Optional[InferenceRunStatus]

        job_id : typing.Optional[str]

        total_predictions : typing.Optional[int]

        total_correct_predictions : typing.Optional[int]

        total_tasks : typing.Optional[int]

        created_at : typing.Optional[dt.datetime]

        triggered_at : typing.Optional[dt.datetime]

        predictions_updated_at : typing.Optional[dt.datetime]

        completed_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferenceRun


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.prompts.versions.create_run(
            id=1,
            version_id=1,
            project=1,
            project_subset="All",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/prompts/{jsonable_encoder(id)}/versions/{jsonable_encoder(version_id)}/inference-runs",
            method="POST",
            json={
                "organization": organization,
                "project": project,
                "model_version": model_version,
                "created_by": created_by,
                "project_subset": project_subset,
                "status": status,
                "job_id": job_id,
                "total_predictions": total_predictions,
                "total_correct_predictions": total_correct_predictions,
                "total_tasks": total_tasks,
                "created_at": created_at,
                "triggered_at": triggered_at,
                "predictions_updated_at": predictions_updated_at,
                "completed_at": completed_at,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(InferenceRun, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncVersionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self,
        id: int,
        *,
        title: str,
        prompt: str,
        provider: PromptVersionProvider,
        provider_model_id: str,
        parent_model: typing.Optional[int] = OMIT,
        created_by: typing.Optional[PromptVersionCreatedBy] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        organization: typing.Optional[PromptVersionOrganization] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PromptVersion:
        """
        Create a new version of a prompt.

        Parameters
        ----------
        id : int
            Prompt ID

        title : str

        prompt : str

        provider : PromptVersionProvider

        provider_model_id : str

        parent_model : typing.Optional[int]

        created_by : typing.Optional[PromptVersionCreatedBy]

        created_at : typing.Optional[dt.datetime]

        updated_at : typing.Optional[dt.datetime]

        organization : typing.Optional[PromptVersionOrganization]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PromptVersion


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.prompts.versions.create(
            id=1,
            title="title",
            prompt="prompt",
            provider="OpenAI",
            provider_model_id="provider_model_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/prompts/{jsonable_encoder(id)}/versions",
            method="POST",
            json={
                "title": title,
                "parent_model": parent_model,
                "prompt": prompt,
                "provider": provider,
                "provider_model_id": provider_model_id,
                "created_by": created_by,
                "created_at": created_at,
                "updated_at": updated_at,
                "organization": organization,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(PromptVersion, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_run(
        self,
        id: int,
        version_id: int,
        *,
        project: int,
        project_subset: InferenceRunProjectSubset,
        organization: typing.Optional[InferenceRunOrganization] = OMIT,
        model_version: typing.Optional[str] = OMIT,
        created_by: typing.Optional[InferenceRunCreatedBy] = OMIT,
        status: typing.Optional[InferenceRunStatus] = OMIT,
        job_id: typing.Optional[str] = OMIT,
        total_predictions: typing.Optional[int] = OMIT,
        total_correct_predictions: typing.Optional[int] = OMIT,
        total_tasks: typing.Optional[int] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        triggered_at: typing.Optional[dt.datetime] = OMIT,
        predictions_updated_at: typing.Optional[dt.datetime] = OMIT,
        completed_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InferenceRun:
        """
        Run a prompt inference.

        Parameters
        ----------
        id : int
            Prompt ID

        version_id : int
            Prompt Version ID

        project : int

        project_subset : InferenceRunProjectSubset

        organization : typing.Optional[InferenceRunOrganization]

        model_version : typing.Optional[str]

        created_by : typing.Optional[InferenceRunCreatedBy]

        status : typing.Optional[InferenceRunStatus]

        job_id : typing.Optional[str]

        total_predictions : typing.Optional[int]

        total_correct_predictions : typing.Optional[int]

        total_tasks : typing.Optional[int]

        created_at : typing.Optional[dt.datetime]

        triggered_at : typing.Optional[dt.datetime]

        predictions_updated_at : typing.Optional[dt.datetime]

        completed_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferenceRun


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.prompts.versions.create_run(
            id=1,
            version_id=1,
            project=1,
            project_subset="All",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/prompts/{jsonable_encoder(id)}/versions/{jsonable_encoder(version_id)}/inference-runs",
            method="POST",
            json={
                "organization": organization,
                "project": project,
                "model_version": model_version,
                "created_by": created_by,
                "project_subset": project_subset,
                "status": status,
                "job_id": job_id,
                "total_predictions": total_predictions,
                "total_correct_predictions": total_correct_predictions,
                "total_tasks": total_tasks,
                "created_at": created_at,
                "triggered_at": triggered_at,
                "predictions_updated_at": predictions_updated_at,
                "completed_at": completed_at,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(InferenceRun, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
