#!/usr/bin/env python

"""
Copyright (c) 2023 sunw4r (https://github.com/sunw4r)
"""

from lib.core.compat import xrange
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.LOW

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Replaces space character (' ') with a null byte '\0'

    Tested against:
        * Microsoft SQL Server 2019

    Notes:
        * Useful to bypass a protection that i dont know what is.

    >>> tamper('SELECT id FROM users')
    'SELECT\0id\0FROM\0users'
    """

    retVal = payload

    if payload:
        retVal = ""
        quote, doublequote, firstspace = False, False, False

        for i in xrange(len(payload)):
            if not firstspace:
                if payload[i].isspace():
                    firstspace = True
                    retVal += "\0"
                    continue

            elif payload[i] == '\'':
                quote = not quote

            elif payload[i] == '"':
                doublequote = not doublequote

            elif payload[i] == " " and not doublequote and not quote:
                retVal += "\0"
                continue

            retVal += payload[i]

    return retVal
