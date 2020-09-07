# coding: utf-8


import pprint
import re  # noqa: F401

import six


class Body39(object):
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
        'tag_name': 'str',
        'name': 'str',
        'body': 'str',
        'prerelease': 'bool'
    }

    attribute_map = {
        'access_token': 'access_token',
        'tag_name': 'tag_name',
        'name': 'name',
        'body': 'body',
        'prerelease': 'prerelease'
    }

    def __init__(self, access_token=None, tag_name=None, name=None, body=None, prerelease=None):  # noqa: E501
        """Body39 - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._tag_name = None
        self._name = None
        self._body = None
        self._prerelease = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        self.tag_name = tag_name
        self.name = name
        self.body = body
        if prerelease is not None:
            self.prerelease = prerelease

    @property
    def access_token(self):
        """Gets the access_token of this Body39.  # noqa: E501

        用户授权码  # noqa: E501

        :return: The access_token of this Body39.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this Body39.

        用户授权码  # noqa: E501

        :param access_token: The access_token of this Body39.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def tag_name(self):
        """Gets the tag_name of this Body39.  # noqa: E501

        Tag 名称, 提倡以v字母为前缀做为Release名称，例如v1.0或者v2.3.4  # noqa: E501

        :return: The tag_name of this Body39.  # noqa: E501
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        """Sets the tag_name of this Body39.

        Tag 名称, 提倡以v字母为前缀做为Release名称，例如v1.0或者v2.3.4  # noqa: E501

        :param tag_name: The tag_name of this Body39.  # noqa: E501
        :type: str
        """
        if tag_name is None:
            raise ValueError("Invalid value for `tag_name`, must not be `None`")  # noqa: E501

        self._tag_name = tag_name

    @property
    def name(self):
        """Gets the name of this Body39.  # noqa: E501

        Release 名称  # noqa: E501

        :return: The name of this Body39.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Body39.

        Release 名称  # noqa: E501

        :param name: The name of this Body39.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def body(self):
        """Gets the body of this Body39.  # noqa: E501

        Release 描述  # noqa: E501

        :return: The body of this Body39.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Body39.

        Release 描述  # noqa: E501

        :param body: The body of this Body39.  # noqa: E501
        :type: str
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

    @property
    def prerelease(self):
        """Gets the prerelease of this Body39.  # noqa: E501

        是否为预览版本。默认: false（非预览版本）  # noqa: E501

        :return: The prerelease of this Body39.  # noqa: E501
        :rtype: bool
        """
        return self._prerelease

    @prerelease.setter
    def prerelease(self, prerelease):
        """Sets the prerelease of this Body39.

        是否为预览版本。默认: false（非预览版本）  # noqa: E501

        :param prerelease: The prerelease of this Body39.  # noqa: E501
        :type: bool
        """

        self._prerelease = prerelease

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
        if issubclass(Body39, dict):
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
        if not isinstance(other, Body39):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other