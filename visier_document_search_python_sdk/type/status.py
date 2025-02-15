# coding: utf-8

"""
    Visier Document Search API

    Visier API for searching for Visier documents

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredStatus(TypedDict):
    pass

class OptionalStatus(TypedDict, total=False):
    # Error classification.
    errorCode: str

    # Error message describing the root cause of the error.
    message: str

class Status(RequiredStatus, OptionalStatus):
    pass
