from django.urls import path
from book.views import Myview1, Myview2, BookListView,Myview3,ContactFormView,BookCreateView,BookListCreateView
from django.shortcuts import render
from book.views import AuthorListCreateView,BookGetUpdateDelete

urlpatterns = [
    path("Myview1/",Myview1),
    path("Myview2/",Myview2.as_view()),
    path("BookListView/",BookListView.as_view()),
    path("Myview3/",Myview3.as_view()),
    path("contact/add", ContactFormView.as_view()),
    path("contact_success/", lambda request: render(request, "success/contact_success.html"), name="contact_success"),
    path("book_form/", BookCreateView.as_view()),
    path("book_successful/", lambda request: render(request, "success/book_successful.html"), name="book_successful"),
    path("book_rest/", BookListCreateView.as_view(),name="book_list_create"),
    path("author_rest/", AuthorListCreateView.as_view(),name="author_list_create"),
    path("rest/book/<int:pk>", BookGetUpdateDelete.as_view(), name="rest_book"),
]
