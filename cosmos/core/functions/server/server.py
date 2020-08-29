"""
Cosmos: A General purpose Discord bot.
Copyright (C) 2020 thec0sm0s
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from . import views
from aiohttp import web


class CosmosServer(object):

    def get_app(self):
        return web.Application(logger=self.bot.log.logger, loop=self.bot.loop)

    async def _init_app(self):
        configs = self.bot.configs.server
        self._runner = web.AppRunner(self.app)
        await self._runner.setup()
        self._http_server = web.TCPSite(
            self._runner, host=configs.host, port=configs.port
        )
        await self._http_server.start()

    def _init_views(self):
        self.app.router.add_routes(web.view(v.ROUTE, v) for v in views.__all__)

    def __init__(self, bot):
        self.bot = bot
        self.app = self.get_app()
        self._runner = None
        self._http_server = None
        self._init_views()
        self.bot.loop.create_task(self._init_app())
