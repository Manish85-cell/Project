from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from .models import User
from .serializers import UserSerializer, CreateUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response

# create your views here.
def main(request):
    return  HttpResponse("Hello, World")


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()      
    serializer_class = UserSerializer  


class CreateUserView(APIView):
    serializer_class = CreateUserSerializer
     
    def post(self, request, format=None):
        pass

 
    
