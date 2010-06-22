from django.conf.urls.defaults import *

urlpatterns = patterns('loans.views',
    url(r'^books', 'books', name = 'books_list'),
)
