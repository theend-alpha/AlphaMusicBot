#
# Copyright (C) 2021-2022 by theend-alpha@Github, < https://github.com/theend-alpha >.
#
# This file is part of < https://github.com/theend-alpha/AlphaMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/theend-alpha/AlphaMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import os
import sys
from os import listdir, mkdir

from ..logging import LOGGER


def dirr():
    if "assets" not in listdir():
        LOGGER(__name__).warning(
            f"Assets Folder not Found. Please clone repository again."
        )
        sys.exit()
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".jpeg"):
            os.remove(file)
    if "downloads" not in listdir():
        mkdir("downloads")
    if "cache" not in listdir():
        mkdir("cache")
    LOGGER(__name__).info("Directories Updated.")
