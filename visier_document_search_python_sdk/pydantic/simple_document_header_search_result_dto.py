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
from pydantic import BaseModel, Field, RootModel

from visier_document_search_python_sdk.pydantic.document_search_link_dto import DocumentSearchLinkDTO

class SimpleDocumentHeaderSearchResultDTO(BaseModel):
    # The `Web Template Framework` representation of the search result element. This commonly displayed alongside the result by search portals.
    description: typing.Optional[str] = Field(None, alias='description')

    # The display name of the element in the search result.
    display_name: typing.Optional[str] = Field(None, alias='displayName')

    # The relevance of the search result and a number between `0` and `100`.
    relevance: typing.Optional[typing.Union[int, float]] = Field(None, alias='relevance')

    # Use the `viewLink` to build a web request to view this document.
    view_link: typing.Optional[DocumentSearchLinkDTO] = Field(None, alias='viewLink')
    class Config:
        arbitrary_types_allowed = True
