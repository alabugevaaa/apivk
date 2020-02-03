import os
import requests



APP_ID = os.getenv('VK_APP_ID')
TOKEN = os.getenv('VK_TOKEN')
BASE_URL = 'https://oauth.vk.com/authorize'
auth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'response_type': 'token',
    'scope': 'friends',
    'v': '5.95'
}

# print('?'.join((BASE_URL, urlencode(auth_data))))

class User:
    def __init__(self, user_id='0'):
        self.token = TOKEN
        self.user_id = user_id

    def __repr__(self):
        return f'https://vk.com/id{self.user_id}'

    def get_params(self):
        return dict(
            access_token=self.token,
            v='5.95'
        )

    def get_friends(self, user_id):
        params = self.get_params()
        params['user_id'] = user_id
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params
        )
        return response.json()['response']['items']

    def __and__(self, other):
        friends1 = self.get_friends(self.user_id)
        friends2 = self.get_friends(other.user_id)

        intersection = set(friends1) & set(friends2)
        common_friends = []
        for i in intersection:
            common_friends.append(User(i))

        return common_friends


Artem = User('579885')
print(f'Артем: {Artem}')
Anya = User('4746274')
print(f'Аня: {Anya}')
common_friends = Artem & Anya
print(f'Общие друзья: {common_friends}')
