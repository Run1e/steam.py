"""Licensed under The MIT License (MIT) - Copyright (c) 2020-present James H-B. See LICENSE"""

from __future__ import annotations

from collections.abc import Coroutine
from ipaddress import IPv4Address
from typing import Any, Generic, TypeVar, final

from typing_extensions import TypeAlias, TypedDict
from yarl import URL

T = TypeVar("T")


@final
class ResponseDict(TypedDict, Generic[T]):
    response: T


Coro: TypeAlias = "Coroutine[Any, Any, T]"
ResponseType: TypeAlias = "Coro[ResponseDict[T]]"
StrOrURL: TypeAlias = URL | str
IPAdress: TypeAlias = IPv4Address


class CMList(TypedDict):
    success: bool
    serverlist: list[CM]


class CM(TypedDict):
    endpoint: str
    load: float
    wtd_load: float


class EResultSuccess(TypedDict):
    sucess: int
