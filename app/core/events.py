#  Copyright 2022 Pavel Suprunov
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from typing import Callable
from fastapi import FastAPI
from loguru import logger

from app.core.settings.app import AppSettings
from app.database.events import close_db_connection, connect_to_db


def create_start_app_handler(app: FastAPI, settings: AppSettings) -> Callable:
    async def start_app() -> None:
        await connect_to_db(app, settings)

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    @logger.catch
    async def stop_app() -> None:
        await close_db_connection(app)

    return stop_app
