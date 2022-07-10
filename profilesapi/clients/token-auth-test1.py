from pydoc import cli
import requests

def client():
    token_h = 'Token 8b980f1ffcbefa382b6f35b737ff2766292ea94f'
    # credentials = {'username': 'admin', 'password': 'admin'}

    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/login/', data=credentials)

    headers = {'Authorization': token_h}

    response = requests.get('http://127.0.0.1:8000/api/profiles/',headers=headers)
    print('Status code: ', response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == '__main__':
    client()