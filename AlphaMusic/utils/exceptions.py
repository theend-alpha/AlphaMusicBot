#
# Copyright (C) 2021-2022 by theend-alpha@Github, < https://github.com/theend-alpha >.
#
# This file is part of < https://github.com/theend-alpha/AlphaMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/theend-alpha/AlphaMusicBot/blob/master/LICENSE >
#
# All rights reserved.


class AssistantErr(Exception):
    def __init__(self, errr: str):
        super().__init__(errr)
