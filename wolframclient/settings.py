# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from wolframclient.utils.datastructures import Settings

NOT_PROVIDED = object()

settings = Settings(
    DEBUG                      = False,
    NORMALIZATION_FUNCTION     = None,
)