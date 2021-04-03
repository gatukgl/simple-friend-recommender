from django.test import TestCase
from django.urls import reverse


class TestQuestion0View(TestCase):
    def test_question_0_view_should_have_some_random_text(self):
        url = reverse('questions:question_0')
        response = self.client.get(url)
        assert 'Question 0' in str(response.content)


class TestQuestion1View(TestCase):
    def test_question_1_view_should_have_some_random_text(self):
        url = reverse('questions:question_1')
        response = self.client.get(url)
        assert 'Question 1' in str(response.content)
