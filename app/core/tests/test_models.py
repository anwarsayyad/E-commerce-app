"""Writing tests for models"""

from django.test import TestCase
from core.models import (
    Items,
)

class Model_tests(TestCase):
    """Class for model test cases"""

    def test_for_creating_items(self):
        item = Items.objects.create(
            title='Test object',
            price=100,
            category='S',
            label='P',
            description='Testing first object'
        )

        self.assertEqual(Items.objects.all().count(), 1)
    