import requests
import unittest

YA_URL = 'https://cloud-api.yandex.net'
YA_TOKEN = 'AQAAAABWIjwmAADLWzDG1ye44UbuoSrd_Blt39Y'


def get_header(api_key=YA_TOKEN):
    return {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {api_key}'
    }

class TestMakeYaDir(unittest.TestCase):

    def test_mk_dir(self):
        dir_name = "777123"
        dir_url = f'{YA_URL}/v1/disk/resources'
        headers = get_header()
        params = {'path': dir_name, 'overwrite': 'true'}
        response = requests.put(dir_url, headers=headers, params=params)

        self.assertTrue(response.status_code == 201)

    def test_dir_exist(self):
        dir_name = "77712"
        dir_url = f'{YA_URL}/v1/disk/resources'
        headers = get_header()
        params = {'path': dir_name, 'overwrite': 'true'}
        response = requests.put(dir_url, headers=headers, params=params)

        self.assertTrue(response.status_code == 409)

