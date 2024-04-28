from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Repair, SamsungRepair,InfinixRepair,IphoneRepair,OppoRepair,XiomiRepair,RealmeRepair,RedmiRepair,TecnoRepair
from .serializers import ProductSerializer, RepairSerializer,XiomiRepairSerializer, IphoneRepairSerializer, RealmeRepairSerializer, RedmiRepairSerializer, OppoRepairSerializer, InfinixRepairSerializer, TecnoRepairSerializer,SamsungRepairSerializer
import json
from django.shortcuts import get_object_or_404
import datetime

from django.http.response import JsonResponse
from django.core.files.storage import default_storage


@api_view(['GET', 'POST', 'DELETE'])
def store(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
       
        products= Product.objects.get(DepartmentId=id)
        products.delete()
        return Response('Deleted Successfully', safe=False)

        product_id = request.data.get('id')  # Assuming you send the product ID in the request data
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST', 'DELETE'])
def service(request):
    if request.method == 'GET':
        repairs = Repair.objects.all()
        serializer = RepairSerializer(repairs, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = RepairSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        # Rename the variable for the specific Repair instance you want to delete, e.g., `repair_to_delete`
        repair_id = request.data.get('id')  # Assuming you send the Repair ID in the request data
        try:
            repairs = Repair.objects.get(id=repair_id)
            repairs.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Repair.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET', 'POST', 'DELETE'])
def iphonerepairs(request):
    if request.method == 'GET':
        iphonerepair = IphoneRepair.objects.all()
        serializer = IphoneRepairSerializer(iphonerepair, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = IphoneRepairSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        
        repair_id = request.data.get('id')  # Assuming you send the Repair ID in the request data
        try:
            iphonerepair = IphoneRepair.objects.get(id=repair_id)
            iphonerepair.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except IphoneRepair.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET', 'POST', 'DELETE'])
def samsungrepairs(request):
    if request.method == 'GET':
        samsungrepair = SamsungRepair.objects.all()
        serializer = SamsungRepairSerializer(samsungrepair, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SamsungRepairSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        
        repair_id = request.data.get('id')  # Assuming you send the Repair ID in the request data
        try:
            samsungrepair = SamsungRepair.objects.get(id=repair_id)
            samsungrepair.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except SamsungRepair.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST', 'DELETE'])
def opporepairs(request):
    if request.method == 'GET':
        opporepair = OppoRepair.objects.all()
        serializer = OppoRepairSerializer(opporepair, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = OppoRepairSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        
        repair_id = request.data.get('id')  # Assuming you send the Repair ID in the request data
        try:
            opporepair = OppoRepair.objects.get(id=repair_id)
            opporepair.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except OppoRepair.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST', 'DELETE'])
def xiomirepairs(request):
    if request.method == 'GET':
        xiomirepair = XiomiRepair.objects.all()
        serializer = XiomiRepairSerializer(xiomirepair, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = XiomiRepairSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        
        repair_id = request.data.get('id')  # Assuming you send the Repair ID in the request data
        try:
            xiomirepair = XiomiRepair.objects.get(id=repair_id)
            xiomirepair.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except XiomiRepair.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST', 'DELETE'])
def realmerepairs(request):
    if request.method == 'GET':
        realmerepair = RealmeRepair.objects.all()
        serializer = RealmeRepairSerializer(realmerepair, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = RealmeRepairSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        
        repair_id = request.data.get('id')  # Assuming you send the Repair ID in the request data
        try:
            realmerepair = RealmeRepair.objects.get(id=repair_id)
            realmerepair.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except RealmeRepair.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST', 'DELETE'])
def infinixrepairs(request):
    if request.method == 'GET':
        infinixrepair = InfinixRepair.objects.all()
        serializer = InfinixRepairSerializer(infinixrepair, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = InfinixRepairSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        
        repair_id = request.data.get('id')  # Assuming you send the Repair ID in the request data
        try:
            infinixrepair = RealmeRepair.objects.get(id=repair_id)
            infinixrepair.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except InfinixRepair.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST', 'DELETE'])
def tecnorepairs(request):
    if request.method == 'GET':
        tecnorepair = TecnoRepair.objects.all()
        serializer = TecnoRepairSerializer(tecnorepair, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TecnoRepairSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        
        repair_id = request.data.get('id')  # Assuming you send the Repair ID in the request data
        try:
            tecnorepair = TecnoRepair.objects.get(id=repair_id)
            tecnorepair.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except TecnoRepair.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST', 'DELETE'])
def redmirepairs(request):
    if request.method == 'GET':
        redmirepair = RedmiRepair.objects.all()
        serializer = RedmiRepairSerializer(redmirepair, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = RedmiRepairSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        
        repair_id = request.data.get('id')  # Assuming you send the Repair ID in the request data
        try:
            redmirepair = RedmiRepair.objects.get(id=repair_id)
            redmirepair.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except RedmiRepair.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
