# coding: utf-8

"""
    IIMMPACT API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2020-09-14T13:01:14Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from iimmpact.api_client import ApiClient


class MyAccountApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_auth_change_password_post(self, new_password_request, **kwargs):  # noqa: E501
        """v1_auth_change_password_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_auth_change_password_post(new_password_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChangePasswordRequest new_password_request: (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_auth_change_password_post_with_http_info(new_password_request, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_auth_change_password_post_with_http_info(new_password_request, **kwargs)  # noqa: E501
            return data

    def v1_auth_change_password_post_with_http_info(self, new_password_request, **kwargs):  # noqa: E501
        """v1_auth_change_password_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_auth_change_password_post_with_http_info(new_password_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChangePasswordRequest new_password_request: (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['new_password_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_auth_change_password_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'new_password_request' is set
        if ('new_password_request' not in params or
                params['new_password_request'] is None):
            raise ValueError("Missing the required parameter `new_password_request` when calling `v1_auth_change_password_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'new_password_request' in params:
            body_params = params['new_password_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['SSO']  # noqa: E501

        return self.api_client.call_api(
            '/v1/auth/change-password', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_auth_new_password_challenge_post(self, new_password_request, **kwargs):  # noqa: E501
        """v1_auth_new_password_challenge_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_auth_new_password_challenge_post(new_password_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NewPasswordRequest new_password_request: (required)
        :return: NewPasswordResponses
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_auth_new_password_challenge_post_with_http_info(new_password_request, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_auth_new_password_challenge_post_with_http_info(new_password_request, **kwargs)  # noqa: E501
            return data

    def v1_auth_new_password_challenge_post_with_http_info(self, new_password_request, **kwargs):  # noqa: E501
        """v1_auth_new_password_challenge_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_auth_new_password_challenge_post_with_http_info(new_password_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NewPasswordRequest new_password_request: (required)
        :return: NewPasswordResponses
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['new_password_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_auth_new_password_challenge_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'new_password_request' is set
        if ('new_password_request' not in params or
                params['new_password_request'] is None):
            raise ValueError("Missing the required parameter `new_password_request` when calling `v1_auth_new_password_challenge_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'new_password_request' in params:
            body_params = params['new_password_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/auth/new-password-challenge', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NewPasswordResponses',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_balance_get(self, **kwargs):  # noqa: E501
        """v1_balance_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_balance_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_balance_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_balance_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_balance_get_with_http_info(self, **kwargs):  # noqa: E501
        """v1_balance_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_balance_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_balance_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['SSO']  # noqa: E501

        return self.api_client.call_api(
            '/v1/balance', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
