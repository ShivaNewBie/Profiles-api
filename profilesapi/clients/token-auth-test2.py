from pydoc import cli
import requests

def client():
    # data = {
    # 'username': 'Shiva',
    # 'email':'test@rest.com',
    # 'password1': 'changeme123',
    # 'password2': 'changeme123'


    # }

    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/registration/', data=data)
    
    token_h = 'Token bf419c4fe5b0bdc52f5db619fa8dedfc7ecff7cb'
    headers = {'Authorization': token_h}
    response = requests.get('http://127.0.0.1:8000/api/profiles/',headers=headers)
    
    print('Status code: ', response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == '__main__':
    client()