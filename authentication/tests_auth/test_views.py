from django.test import TestCase, Client
from django.urls import reverse
from authentication.models import MyUser
import json

class TestViews(TestCase):

    def test_user_connection(self):
        pass