from django.test import TestCase
from event_finder.models import Users

class UsersTestCase(TestCase):
    def setUp(self):
        Users.objects.create(user_id='0', user_username = 'firstUser', user_password = 'firstaccount')
        Users.objects.create(user_id='1', user_username = 'secondUser', user_password = 'secondaccount')

