"""
Test custom Django mana
"""

from unittest.mock import patch
from psycopg2 import OperationalError as Pycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

class CommandTests(SimpleTestCase):
    """Test commands."""

    def test_wait_for_db_ready(self):
        