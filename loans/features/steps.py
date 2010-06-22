from freshen import *
from loans.models import Book

from django.test.client import Client

@Given('there are (\d+) books in the system')
def create_books(total_of_books):
    scc.books = []
    for i in xrange(int(total_of_books)):
        book = Book()
        book.title = 'Book %d' %(i + 1)
        book.author = 'Francisco Souza'
        book.save()
        scc.books.append(book)

@When('I navigate to the books list page')
def navigate_to_books_list():
    client = Client()
    scc.response = client.get('/loan/books')
