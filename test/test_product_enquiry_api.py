# coding: utf-8

"""
    IIMMPACT API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2020-09-14T13:01:14Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import iimmpact
from iimmpact.api.product_enquiry_api import ProductEnquiryApi  # noqa: E501
from iimmpact.rest import ApiException


class TestProductEnquiryApi(unittest.TestCase):
    """ProductEnquiryApi unit test stubs"""

    def setUp(self):
        self.api = iimmpact.api.product_enquiry_api.ProductEnquiryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_products_get(self):
        """Test case for v1_products_get

        """
        pass


if __name__ == '__main__':
    unittest.main()
