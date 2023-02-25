from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Account


@api_view(["GET", "POST"])
def getAccountList(request):
    if request.method == "GET":
        accounts = Account.objects.using("account_service").all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if reques.method == "POST":
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(using="account_service")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def getAccountDetails(request, pk):
    try:
        account = Account.objects.using("account_service").get(pk=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save(using="account_service")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        account.delete(using="account_service")
        return Response(status=status.HTTP_204_NO_CONTENT)
