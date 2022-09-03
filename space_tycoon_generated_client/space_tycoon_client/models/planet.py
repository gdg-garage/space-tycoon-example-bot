# coding: utf-8

"""
    Space Tycoon

    Space Tycoon server.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Planet(object):
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
        'name': 'str',
        'resources': 'dict(str, TradingResource)',
        'position': 'Coordinates',
        'prev_position': 'Coordinates'
    }

    attribute_map = {
        'name': 'name',
        'resources': 'resources',
        'position': 'position',
        'prev_position': 'prevPosition'
    }

    def __init__(self, name=None, resources=None, position=None, prev_position=None):  # noqa: E501
        """Planet - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._resources = None
        self._position = None
        self._prev_position = None
        self.discriminator = None
        self.name = name
        self.resources = resources
        self.position = position
        self.prev_position = prev_position

    @property
    def name(self):
        """Gets the name of this Planet.  # noqa: E501


        :return: The name of this Planet.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Planet.


        :param name: The name of this Planet.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def resources(self):
        """Gets the resources of this Planet.  # noqa: E501


        :return: The resources of this Planet.  # noqa: E501
        :rtype: dict(str, TradingResource)
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this Planet.


        :param resources: The resources of this Planet.  # noqa: E501
        :type: dict(str, TradingResource)
        """
        if resources is None:
            raise ValueError("Invalid value for `resources`, must not be `None`")  # noqa: E501

        self._resources = resources

    @property
    def position(self):
        """Gets the position of this Planet.  # noqa: E501


        :return: The position of this Planet.  # noqa: E501
        :rtype: Coordinates
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Planet.


        :param position: The position of this Planet.  # noqa: E501
        :type: Coordinates
        """
        if position is None:
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501

        self._position = position

    @property
    def prev_position(self):
        """Gets the prev_position of this Planet.  # noqa: E501


        :return: The prev_position of this Planet.  # noqa: E501
        :rtype: Coordinates
        """
        return self._prev_position

    @prev_position.setter
    def prev_position(self, prev_position):
        """Sets the prev_position of this Planet.


        :param prev_position: The prev_position of this Planet.  # noqa: E501
        :type: Coordinates
        """
        if prev_position is None:
            raise ValueError("Invalid value for `prev_position`, must not be `None`")  # noqa: E501

        self._prev_position = prev_position

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
        if issubclass(Planet, dict):
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
        if not isinstance(other, Planet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other