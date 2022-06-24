import imp
from pickle import FRAME
from xmlrpc.client import ResponseError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

from .models import Books, Authors
from .serializers import BooksSerializers, AuthorsSerializers

# Create your views here.
@api_view(['GET', 'POST'])
def getBooks(request):
    if request.method == 'GET':
        books = Books.objects.all()
        books_serializer = BooksSerializers(books, many = True)
        return JsonResponse(books_serializer.data, safe= False)
    elif request.method == 'POST':
        books_serializer = BooksSerializers(data = request.data)
        if books_serializer.is_valid():
            return Response(books_serializer.data, status = status.HTTP_201_CREATED)
        
def welcomePage(request):
    if request.method == 'GET':
        return Response('Welcome to Group 10\'s bookstore API!', safe= False)