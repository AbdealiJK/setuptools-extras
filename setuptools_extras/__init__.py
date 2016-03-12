# -*- coding: utf-8 -*-

import os

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(PROJECT_PATH, "VERSION")) as fp:
    __version__ = fp.read().strip()
