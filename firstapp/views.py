from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User


@api_view(['POST'])
def registrationAPI(request):
    if request.method == 'POST':
        username = request.data['username']
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password1 = request.data['password1']
        password2 = request.data['password2']

    if User.objects.filter(username=username).exists():
        return Response({"error": "An user with this username already exists!"},headers={'Access-Control-Allow-Origin': 'http://127.0.0.1:5500'})
   
    if User.objects.filter(email=email).exists():
        return Response({"error": "An user with this email already exists!"},headers={'Access-Control-Allow-Origin': 'http://127.0.0.1:5500'})
   
    if password1 != password2:
        return Response({"error": "Two Password didn't match"},headers={'Access-Control-Allow-Origin': 'http://127.0.0.1:5500'})
    
    user = User()
    user.username=username
    user.email=email
    user.first_name=first_name
    user.last_name=last_name
    user.is_active=True
    user.set_password(raw_password=password1)
    user.save()

    return Response({'success': 'User successfully resisterd!'},headers={'Access-Control-Allow-Origin': 'http://127.0.0.1:5500'})



@api_view(['GET', 'POST'])
def firstAPI(request):
    if request.method=='POST':
        name = request.data['name']
        age = request.data['age']
        print(name, age)
        return Response({'name': name, 'age':age})
    context = {
        'name': 'Shahid Afridi',
        'country': 'Bangladesh'
    }
    return Response(context,headers={'Access-Control-Allow-Origin': 'http://127.0.0.1:5500'})


