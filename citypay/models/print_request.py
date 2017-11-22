# coding: utf-8

"""
    CityPay POS API

    CityPay Point of Sale API for payment with card present devices including EMV readers and contactless POS readers.  The API makes it simple to add EMV and contactless card acceptance to iOS, Android, Tablet and desktop applicaitons using a HTTPS protocol. It segregates the complexity of payment processing from the sales environment and eliminates any necessity for the target system to handle card data.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: dev@citypay.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PrintRequest(object):
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
        'identifier': 'str',
        'type': 'str'
    }

    attribute_map = {
        'identifier': 'identifier',
        'type': 'type'
    }

    def __init__(self, identifier=None, type=None):  # noqa: E501
        """PrintRequest - a model defined in Swagger"""  # noqa: E501

        self._identifier = None
        self._type = None
        self.discriminator = None

        self.identifier = identifier
        if type is not None:
            self.type = type

    @property
    def identifier(self):
        """Gets the identifier of this PrintRequest.  # noqa: E501

        Must include an identifier for a transaction that has been carried out on the device  # noqa: E501

        :return: The identifier of this PrintRequest.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this PrintRequest.

        Must include an identifier for a transaction that has been carried out on the device  # noqa: E501

        :param identifier: The identifier of this PrintRequest.  # noqa: E501
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def type(self):
        """Gets the type of this PrintRequest.  # noqa: E501

        The instruction prints the cardholder copy of the receipt by default. If you want to reprint the merchant copy, append “type”:”merchant” to the body of the request.  # noqa: E501

        :return: The type of this PrintRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PrintRequest.

        The instruction prints the cardholder copy of the receipt by default. If you want to reprint the merchant copy, append “type”:”merchant” to the body of the request.  # noqa: E501

        :param type: The type of this PrintRequest.  # noqa: E501
        :type: str
        """

        self._type = type

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PrintRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
