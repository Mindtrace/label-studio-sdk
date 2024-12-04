# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1


class BaseUser(pydantic_v1.BaseModel):
    id: typing.Optional[int] = None
    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    username: str
    email: typing.Optional[str] = None
    last_activity: typing.Optional[dt.datetime] = None
    avatar: typing.Optional[str] = None
    initials: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    active_organization: typing.Optional[int] = None
    allow_newsletters: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Allow sending newsletters to user
    """

    date_joined: typing.Optional[dt.datetime] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
