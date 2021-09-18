from rest_framework.test import APITestCase

from django.contrib.auth.models import User

from users.models import User as UserModel


class UserTestCase(APITestCase):

    def setUP(self):
        self.host = 'http//127.0.0.1:8000'
        self.user = UserModel.objects.create(name='New user', age='20', happy=True, healthy=True, busy=True)
        User.objects.create_user(username='user', password='password', is_staff=True)
        response = self.client.post(f'{self.host}/api/token/', data={'username': 'user', 'password': 'password'})
        assert response.status_code == 200, response.status_code
        self.token = response.data['access']

    def test_get_user(self):
        response = self.client.get(f'{self.host}/users/')
        self.assertNotEqual(len(response.data), 0)

    """def test_create_user(self):
        response = self.client.post(f'{self.host}/users/',
                                    data={'name': 'New user', 'age': '20', 'happy': 'True', 'healthy': 'True', 'busy': 
                                    'True'},
                                    HTTP_AUTHORIZATION=f'{self.token}')
        self.assertEqual(response.status_code, 201)
        total_users = UserModel.objects.all().count()
        self.assertEqual(total_users, 0)"""