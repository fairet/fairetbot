#    Friendly Discord (discord userbot)
#    Copyright (C) The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

# ©️ Fairet, 2021-2023
# This file is a part of Fairet bot
# 🌐 https://github.com/fairet/fairetbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# 🔑 https://www.gnu.org/licenses/agpl-3.0.html

import discord
import os
import json

from discord.ext import commands

client = commands.Bot(command_prefix=".")

def main():
    request = str(input("::Enter: "))
    print(load_from_json(request))

def load_from_json(setting):
    with open("config.json", "r") as file:
        parsed = json.load(file)
        file.close()
    
    data = parsed["config"][setting]
    
    return data

if __name__ == "__main__":
    main()