import requests

def get_token():
    tokenEndPoint = f'{baseURL}/api/token/'
    response = requests.post(tokenEndPoint, data={'username': 'admin', 'password': 'app123'})
    token = response.json()['access']
    return token

#get data
def get_data():
    getEndPoint = f'{baseURL}/api/users_list/'
    header = {'Authorization': f'Bearer {get_token()}'}
    response = requests.get(getEndPoint, headers = header)
    emp_data = response.json()
    for e in emp_data:
        print(e)

#post(add) data
def post_data(seq):
    postEndPoint = f'{baseURL}/api/users_list/'
    header = {'Authorization': f'Bearer {get_token()}'}
    data = {
        'employeeID': f'HQ00{seq}', 'employeeName': f'Test user {seq}', 'ranking': 6.8 + seq, 'age': 68 + seq
    }
    response = requests.post(postEndPoint, data = data, headers = header)
    print(response.text, response.status_code)

#edit data
def edit_data(employeeID, employeeName, ranking, age):
    editEndPoint = f'{baseURL}/api/users_list/{employeeID}/'
    header = {'Authorization': f'Bearer {get_token()}'}
    data = {
        'employeeName': f'{employeeName}', 'ranking': {ranking}, 'age': {age}
    }
    response = requests.put(editEndPoint, data = data, headers = header)
    print(response.text, response.status_code)

#delete data
def delete_data(employeeID):
    deleteEndPoint = f'{baseURL}/api/users_list/{employeeID}/'
    header = {'Authorization': f'Bearer {get_token()}'}
    response = requests.delete(deleteEndPoint, headers = header)
    print(response.text, response.status_code)

if __name__ == "__main__":
    baseURL = 'http://127.0.0.1:8000'
    # print(get_token())
    post_data(11)
    get_data()

