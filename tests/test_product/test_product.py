from tests.base import CommonTestCases, TestConfiguration
from fixtures.product.product_fixture import (
    create_product_mutation, create_product_response,
    edit_product_mutation, edit_product_response,
    delete_product_mutation, delete_product_response
)


class TestProductMutation(TestConfiguration):

    def test_create_product(self):
        CommonTestCases.get_response_with_token(
            self, create_product_mutation, create_product_response)

    def test_edit_product(self):
        CommonTestCases.get_response_with_token(
            self, edit_product_mutation, edit_product_response)

    def test_delete_product(self):
        CommonTestCases.get_response_with_token(
            self, delete_product_mutation, delete_product_response)
