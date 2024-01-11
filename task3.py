import time
from progress.bar import ChargingBar
import requests
import json
from urllib.parse import urlencode

bar = ChargingBar('Processing', max=6)

# создание папки
token = 'y0_AgAAAABwaeWcAArJwgAAAADxZlDZay0mpBexSP2DLqRlsHUzh2GpDkw'
headers = {'Authorization': token}
params = {'path': 'img'}
response = requests.put('https://cloud-api.yandex.net/v1/disk/resources', params=params, headers=headers)

# для заполнения пользователем
user_id = '287717301'
token_vk = ('vk1.a.EBgHhofyNXB8fAvWKQ9irK-MQOiuiWqf7Rz5wcc8NKMI0_JQG5m8OU4jsZYkna6jY1pMgpl0ECHOS2sF-XN5Szo7ZtJxLhv4sC' +
            'xvQZ0bgNg5OoLiEJqOYHpDJeqy0h7lxbgZvEs6edM0UdC4kx3e6zDq7O6gIuI4sDRLfBoox5LrPxgUBGASj63Yhif1tNDQ')
app_id = '51789264'
auth_url = 'https://oauth.vk.com/authorize'
params = {'client_id': app_id,
          'redirect_url': 'https://oauth.vk.com/authorize/blank.html',
          'display': 'page',
          'scope': 'photos',
          'response_type': 'token'}
oauth_url = f'{auth_url}?{urlencode(params)}'
print('Извлеките VK-токен по ссылке: ', oauth_url, end='\n')
bar.next()



class VK:
    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def get_likes(self, item):
        params = {'owner_id': self.id, 'type': 'photo', 'access_token': token_vk, 'v': '5.131', 'item_id': item}
        response = requests.get('https://api.vk.com/method/likes.getList', params=params)
        return response.json()

    def get_photos(self):
        params = self.params
        params.update({'user_id': self.id, 'album_id': 'profile'})
        response = requests.get('https://api.vk.com/method/photos.get', params=params)
        return response.json()


photos = dict()
counter = 0
vk = VK(token_vk, user_id)
for each in vk.get_photos()['response']['items']:
    for size in each['sizes']:
        if size['type'] == 'z' and counter < 5:
            bar.next()
            counter += 1
            response = requests.get(size['url'])
            params = {'path': 'img/' + str(vk.get_likes(each['id'])['response']['count']) + '.jpg'}
            response_ = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload', params=params,
                                     headers=headers)
            url_for_upload = response_.json().get('href')
            res = requests.put(url_for_upload, files={'file': response.content})
            photos.setdefault('item' + str(counter),
                              [{"file_name": str(vk.get_likes(each['id'])['response']['count']) + '.jpg'},
                               {'size': size['type']}])

with open('photos.json', 'w') as file:
    file.write(json.dumps(photos))

bar.finish()