from django.test import TestCase

from .auth_test import AuthModelTest
from .database_massage_test import MessageModelTest
from .database_auth_test import AuthDbModelTest
from .weather_test import WeatherModelTest
from .chatbot_test import ChatbotModelTest
from .database_test import BaseModelTest

class TestAllModels(TestCase):
    AuthModelTest()
    MessageModelTest()
    BaseModelTest()
    WeatherModelTest()
    ChatbotModelTest()