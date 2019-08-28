login_mutation = '''
    mutation {
        loginUser(name: "Ken", password: "1234567") {
        token
        }
    }
'''

login_mutation_response = {"data": {"loginUser": {"token": "b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJkZWZhdWx0IiwibmFtZSI6IktlbiJ9.FV8PUtBAPLUsn-TXXR1RtGjcaUTcYdq7PmBwb0OT9BE'"}}}  # noqa

sign_up_mutation = '''
    mutation{
        createUser(name:"Ken", password:"1234567", confirmPassword:"1234567"){
        user{
            name
        }
        }
    }
'''

sign_up_response = {"data": {"createUser": {"user": {"name": "Ken"}}}}

query_users = '''
    query{
        allUsers{
            name
        }
    }
'''

query_user_response = {"data": {"allUsers": [{"name": "Ken"}]}}
