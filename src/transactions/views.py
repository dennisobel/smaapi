from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from transactions.models import Transaction, Quarter, Corridor
from transactions.serializers import TransactionSerializer
import json


@api_view(['GET','POST'])
def transaction_list(request):    
    if request.method == 'GET':        
        quarters = Transaction.objects.all().values("quarter_id")
        quarter_array = [quarter["quarter_id"] for quarter in quarters]
              
        
        '''Return latest quarter'''
        transactions = Transaction.objects.filter(quarter_id=max(quarter_array))  

        print(transactions.values())
       
        transaction_serializer = TransactionSerializer(transactions, many=True)
        return Response(transaction_serializer.data)

    elif request.method == 'POST':        
        transaction_serializer = TransactionSerializer(data=request.data)
        if transaction_serializer.is_valid():
            transaction_serializer.save()
            return Response(transaction_serializer.data, status=status.HTTP_201_CREATED)
        return Response(transaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST','PUT'])
def transaction_detail(request, pk):
    try:
        transaction = Transaction.objects.get(pk=pk)
    except Transaction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        transaction_serializer = TransactionSerializer(transaction)
        return Response(transaction_serializer.data)

    elif request.method == 'PUT':
        transaction_serializer = TransactionSerializer(transaction, data=request.data)
        if transaction_serializer.is_valid():
            transaction_serializer.save()
            return Response(transaction_serializer.data)
        return Response(transaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
