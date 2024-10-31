#from django
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse #function based
from django.views import View #class based
from django.views.generic import ListView, FormView, CreateView
from django.urls import reverse_lazy
#from rest_framework
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

#from book
from book.models import Book,Author
from book.serializer import BookSerializer, AuthorSerializer
from book.forms import ContactForm, BookForm

# Create your views here.
def Myview1(request):
    return HttpResponse("welcome django1")

class Myview2(View):
    def get(self,request):
        return HttpResponse("welcome django2")

class BookListView(ListView):
    model=Book
    template_name="book_list.html"
    context_object_name="books"
    
class Myview3(View):
    def get(self,request):
        return HttpResponse("welcome django 33333333")
    
class ContactFormView(FormView):
    template_name= "contact.html" 
    form_class=ContactForm
    success_url= reverse_lazy('contact_success') 
    
    def form_valid(self, form) -> HttpResponse:
        return super().form_valid(form)
    
class BookCreateView(CreateView):
    model=Book
    form_class=BookForm
    template_name='book_form.html'
    success_url=reverse_lazy('book_successful')
    

# Rest framework API
class BookListCreateView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    
    def get(self,request):
        print(request.user)
        books=Book.objects.all()
        serializer= BookSerializer(books,many=True)
        data=serializer.data
        return Response(data, status= status.HTTP_200_OK)
    
    def post(self,request):
        # instance=Book.objects.get(id=pk)
        # instance=get_object_or_404(Book,pk=pk)
        serializer= BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
class AuthorListCreateView(APIView):
   
    def get(self,request):
        authors=Author.objects.all()
        serializer=AuthorSerializer(authors,many=True)
        data= serializer.data
        return Response(data,status= status.HTTP_200_OK)
    
    def post(self,request):
        serializer=AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        

class BookGetUpdateDelete(RetrieveModelMixin,UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset= Book.objects.all()
    serializer_class=BookSerializer
    http_method_names=('get','post','put','delete')
    
    def get(self,request,*args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request,*args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self,request,*args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self,request,*args, **kwargs):
        return self.destroy(request, *args, **kwargs)