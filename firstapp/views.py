from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

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
