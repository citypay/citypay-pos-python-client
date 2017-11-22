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
from citypay.api.payment_module_api import PaymentModuleApi  # noqa: E501
from citypay.rest import ApiException


class TestPaymentModuleApi(unittest.TestCase):
    """PaymentModuleApi unit test stubs"""

    def setUp(self):
        self.api = citypay.api.payment_module_api.PaymentModuleApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_receipt(self):
        """Test case for receipt

        Receipt Print  # noqa: E501
        """
        pass

    def test_refund(self):
        """Test case for refund

        Refund Transaction  # noqa: E501
        """
        pass

    def test_reversal(self):
        """Test case for reversal

        Reversal Tranasction  # noqa: E501
        """
        pass

    def test_sale(self):
        """Test case for sale

        Sale Transaction  # noqa: E501
        """
        pass

    def test_transaction(self):
        """Test case for transaction

        Transaction Status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()