from tests.base import CommonTestCases, TestConfiguration
from fixtures.user.user_fixture import (
    login_mutation, login_mutation_response,
    sign_up_mutation, sign_up_response)


class TestAuthMutation(TestConfiguration):

    def test_sign_up_users(self):
        CommonTestCases.get_response(self, sign_up_mutation, sign_up_response)

    def test_sign_in_users(self):
        CommonTestCases.get_response(self,
                                     login_mutation,
                                     login_mutation_response)
