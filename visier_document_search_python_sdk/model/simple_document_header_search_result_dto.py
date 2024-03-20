# coding: utf-8

"""
    Visier Document Search API

    Visier API for searching for Visier documents

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from visier_document_search_python_sdk import schemas  # noqa: F401


class SimpleDocumentHeaderSearchResultDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Structure of a single document header search using the Simple search operation.
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            displayName = schemas.StrSchema
            relevance = schemas.Float64Schema
        
            @staticmethod
            def viewLink() -> typing.Type['DocumentSearchLinkDTO']:
                return DocumentSearchLinkDTO
            __annotations__ = {
                "description": description,
                "displayName": displayName,
                "relevance": relevance,
                "viewLink": viewLink,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relevance"]) -> MetaOapg.properties.relevance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["viewLink"]) -> 'DocumentSearchLinkDTO': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "displayName", "relevance", "viewLink", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relevance"]) -> typing.Union[MetaOapg.properties.relevance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["viewLink"]) -> typing.Union['DocumentSearchLinkDTO', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "displayName", "relevance", "viewLink", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        displayName: typing.Union[MetaOapg.properties.displayName, str, schemas.Unset] = schemas.unset,
        relevance: typing.Union[MetaOapg.properties.relevance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        viewLink: typing.Union['DocumentSearchLinkDTO', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SimpleDocumentHeaderSearchResultDTO':
        return super().__new__(
            cls,
            *args,
            description=description,
            displayName=displayName,
            relevance=relevance,
            viewLink=viewLink,
            _configuration=_configuration,
            **kwargs,
        )

from visier_document_search_python_sdk.model.document_search_link_dto import DocumentSearchLinkDTO
