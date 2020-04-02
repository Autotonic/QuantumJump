# -*- coding: utf-8 -*-
#
# Copyright 2020, JohnnyCarcinogen ( https://github.com/JohnRipper/ ), All rights reserved.
#
# Created by dev at 3/29/20
# This file is part of QuantumJump
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
import asyncio

from lib.cog import Cog
from lib.command import makeCommand, Command

TRUCK = ["──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌",
         "───▄▄██▌█ beep beep",
         "▄▄▄▌▐██▌█ {} delivery",
         "███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄",
         "▀(@)▀▀▀▀▀▀▀(@)( @)▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀(@)▀"]

class Art(Cog):


    @makeCommand(aliases=["deliver", "amazon", "ebay", "craigslist"], description="<str> makes a delivery")
    async def deliver(self, c: Command):
        format_data = "gay porn"
        d = TRUCK.copy()
        if c.message:
            format_data = c.message
        d[2] = d[2].format(format_data)
        for line in d:
            await self.send_message(line)

    @makeCommand(aliases=["fred"], description="makes fred")
    async def fred(self, c: Command):
        f = open("data/sci", "r")
        if f.mode == 'r':
            lines = f.readlines()
            for line in lines:
                await self.send_message(line)
        f.close()

    @makeCommand(aliases=["draw"], description="makes drawing")
    async def draw(self, c: Command):
        # wont work on windows. needs to use os.path.join for directory
        if c.message != "" or c.message is not None:
            f = open(f"data/art/{c.message}", "r")
            if f.mode == 'r':
                lines = f.readlines()
                for line in lines:
                    await self.send_message(line)
                    await asyncio.sleep(.05)

            f.close()