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
    if request.method == 'POST':
        books_serializer = BooksSerializers(data = request.data)
        if books_serializer.is_valid():
            books_serializer.save()
            return Response(books_serializer.data, status = status.HTTP_201_CREATED)
   
@api_view(['GET'])     
def bookISBN(request, ISBN):
    try:
        book = Books.objects.get(pk=ISBN)
    except Books.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        books_serializer = BooksSerializers(book)
        return Response(books_serializer.data)
        
def welcomePage(request):
    if request.method == 'GET':
        return JsonResponse('Welcome to Group 10\'s bookstore API!', safe = False)