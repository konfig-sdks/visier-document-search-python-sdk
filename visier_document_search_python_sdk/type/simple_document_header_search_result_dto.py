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

from visier_document_search_python_sdk.type.document_search_link_dto import DocumentSearchLinkDTO

class RequiredSimpleDocumentHeaderSearchResultDTO(TypedDict):
    pass

class OptionalSimpleDocumentHeaderSearchResultDTO(TypedDict, total=False):
    # The `Web Template Framework` representation of the search result element. This commonly displayed alongside the result by search portals.
    description: str

    # The display name of the element in the search result.
    displayName: str

    # The relevance of the search result and a number between `0` and `100`.
    relevance: typing.Union[int, float]

    # Use the `viewLink` to build a web request to view this document.
    viewLink: DocumentSearchLinkDTO

class SimpleDocumentHeaderSearchResultDTO(RequiredSimpleDocumentHeaderSearchResultDTO, OptionalSimpleDocumentHeaderSearchResultDTO):
    pass
