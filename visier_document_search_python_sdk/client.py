# coding: utf-8
"""
    Visier Document Search API

    Visier API for searching for Visier documents

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from visier_document_search_python_sdk.client_custom import ClientCustom
from visier_document_search_python_sdk.configuration import Configuration
from visier_document_search_python_sdk.api_client import ApiClient
from visier_document_search_python_sdk.type_util import copy_signature
from visier_document_search_python_sdk.apis.tags.document_search_api import DocumentSearchApi



class VisierDocumentSearch(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.document_search: DocumentSearchApi = DocumentSearchApi(api_client)
