# -*- coding: utf-8 -*-

"""A basic integration test"""

import sys

import steam

from . import IDENTITY_SECRET, PASSWORD, SHARED_SECRET, USERNAME


class Client(steam.Client):
    LOGIN = False
    CONNECT = False
    READY = False
    LOGOUT = False

    async def start(self) -> None:
        try:
            await super().start(USERNAME, PASSWORD, shared_secret=SHARED_SECRET, identity_secret=IDENTITY_SECRET)
        except steam.LoginError as exc:
            if "too many login failures" not in exc.args[0]:
                raise exc
            return

    async def on_login(self) -> None:
        self.LOGIN = True

    async def on_connect(self) -> None:
        self.CONNECT = True

    async def on_ready(self) -> None:
        self.READY = True
        await self.close()

    async def on_logout(self) -> None:
        self.LOGOUT = True


def test_basic_events():
    if sys.version_info[:2] == (3, 8):  # only test on 3.9 and 3.7 as that's where the issues normally are
        return
    client = Client()
    client.run()
    assert client.LOGIN
    assert client.CONNECT
    assert client.READY
    assert client.LOGOUT
