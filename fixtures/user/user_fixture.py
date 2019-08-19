login_mutation = '''
    mutation {
        loginUser(name: "Ken", password: "1234567") {
        token
        }
    }
'''

login_mutation_response = {"data": {"loginUser": {"token": "b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiZGVmYXVsdCIsIm5hbWUiOiJLZW4ifQ.hXdn5QjPsoydnyeUIU58CgKeWm869FoY4OVzgg38o0w'"}}}  # noqa

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
