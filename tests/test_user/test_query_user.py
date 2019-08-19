from tests.base import CommonTestCases, TestConfiguration
from fixtures.user.user_fixture import query_users, query_user_response


class TestQueryUsers(TestConfiguration):

    def test_query_users(self):
        CommonTestCases.get_response(self, query_users, query_user_response)
