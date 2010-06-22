# Create your views here.
from models import Book
from django.shortcuts import render_to_response
from django.template import RequestContext

def books(request):
    books = Book.objects.all()
    return render_to_response('books_list.html', {
            'books' : books
        }, context_instance=RequestContext(request)
    )
