from loans.models import Book
from freshen import *
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
    scc.response = client.get('/loans/books')

@Then('I should see the title of the (\d+) books')
def check_presence_of_the_title_of_books(total_of_books):
    expected_string = ''
    for book in scc.books:
        expected_string = '<li>%s</li>' % book.title
    assert_true(expected_string in scc.response.content)
