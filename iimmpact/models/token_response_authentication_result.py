# coding: utf-8

"""
    IIMMPACT API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2020-09-14T13:01:14Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TokenResponseAuthenticationResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'access_token': 'str',
        'expires_in': 'int',
        'token_type': 'str',
        'refresh_token': 'str',
        'id_token': 'str'
    }

    attribute_map = {
        'access_token': 'AccessToken',
        'expires_in': 'ExpiresIn',
        'token_type': 'TokenType',
        'refresh_token': 'RefreshToken',
        'id_token': 'IdToken'
    }

    def __init__(self, access_token=None, expires_in=None, token_type=None, refresh_token=None, id_token=None):  # noqa: E501
        """TokenResponseAuthenticationResult - a model defined in Swagger"""  # noqa: E501

        self._access_token = None
        self._expires_in = None
        self._token_type = None
        self._refresh_token = None
        self._id_token = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if expires_in is not None:
            self.expires_in = expires_in
        if token_type is not None:
            self.token_type = token_type
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if id_token is not None:
            self.id_token = id_token

    @property
    def access_token(self):
        """Gets the access_token of this TokenResponseAuthenticationResult.  # noqa: E501


        :return: The access_token of this TokenResponseAuthenticationResult.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this TokenResponseAuthenticationResult.


        :param access_token: The access_token of this TokenResponseAuthenticationResult.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def expires_in(self):
        """Gets the expires_in of this TokenResponseAuthenticationResult.  # noqa: E501


        :return: The expires_in of this TokenResponseAuthenticationResult.  # noqa: E501
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this TokenResponseAuthenticationResult.


        :param expires_in: The expires_in of this TokenResponseAuthenticationResult.  # noqa: E501
        :type: int
        """

        self._expires_in = expires_in

    @property
    def token_type(self):
        """Gets the token_type of this TokenResponseAuthenticationResult.  # noqa: E501


        :return: The token_type of this TokenResponseAuthenticationResult.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this TokenResponseAuthenticationResult.


        :param token_type: The token_type of this TokenResponseAuthenticationResult.  # noqa: E501
        :type: str
        """

        self._token_type = token_type

    @property
    def refresh_token(self):
        """Gets the refresh_token of this TokenResponseAuthenticationResult.  # noqa: E501


        :return: The refresh_token of this TokenResponseAuthenticationResult.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this TokenResponseAuthenticationResult.


        :param refresh_token: The refresh_token of this TokenResponseAuthenticationResult.  # noqa: E501
        :type: str
        """

        self._refresh_token = refresh_token

    @property
    def id_token(self):
        """Gets the id_token of this TokenResponseAuthenticationResult.  # noqa: E501


        :return: The id_token of this TokenResponseAuthenticationResult.  # noqa: E501
        :rtype: str
        """
        return self._id_token

    @id_token.setter
    def id_token(self, id_token):
        """Sets the id_token of this TokenResponseAuthenticationResult.


        :param id_token: The id_token of this TokenResponseAuthenticationResult.  # noqa: E501
        :type: str
        """

        self._id_token = id_token

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TokenResponseAuthenticationResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TokenResponseAuthenticationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
