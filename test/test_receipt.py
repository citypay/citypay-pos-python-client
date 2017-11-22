# coding: utf-8

"""
    CityPay POS API

    CityPay Point of Sale API for payment with card present devices including EMV readers and contactless POS readers.  The API makes it simple to add EMV and contactless card acceptance to iOS, Android, Tablet and desktop applicaitons using a HTTPS protocol. It segregates the complexity of payment processing from the sales environment and eliminates any necessity for the target system to handle card data.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: dev@citypay.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import citypay
from citypay.models.receipt import Receipt  # noqa: E501
from citypay.rest import ApiException


class TestReceipt(unittest.TestCase):
    """Receipt unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReceipt(self):
        """Test Receipt"""
        # FIXME: construct object with mandatory attributes with example values
        # model = citypay.models.receipt.Receipt()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
