#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from . import *

try:
    APP_ID = config("APP_ID", default=11873433, cast=int)
    API_HASH = config("API_HASH", default="96abaf0d59cd1f5482bdc93ba6030424")
    BOT_TOKEN = config("BOT_TOKEN", default="5269784341:AAFAz_umXmT9iaj5ds5mlZK0Jh0AwaT6hRQ")
    OWNER = config("OWNER_ID", default=148567797, cast=int)
    LOG = config("LOG_CHANNEL", default="-1001341073959", cast=int)
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
