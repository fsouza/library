"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.db import IntegrityError
from nose.tools import *

class BookTest(TestCase):

    def test_model_validation_title_author(self):
        from models import Book
        b = Book(title = None, author = None)
        assert_raises(IntegrityError, b.save)

