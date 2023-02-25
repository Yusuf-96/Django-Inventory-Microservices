from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Account

@api_view(['GET'])
def getAccountList(request):
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(seriaizer.data, status = status.HTTP_200_OK)
    
@api_view(['GET'])
def getAccountDetails(request, pk):
    if request.method == 'GET':
        account = Account.objects.get(pk = pk)
        serializer = AccountSerializer(account)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
