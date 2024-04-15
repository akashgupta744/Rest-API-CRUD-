from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from app.serializers import *
from rest_framework import status

# Create your views here.

class CategoryCrud(APIView):
    def get(self, request,id):
        CDO = Category.objects.all()
        CJO = CategoryModelSerializer(CDO, many = True)
        return Response(CJO.data)
    
    def post(self,request,id):
        JDO = request.data
        CDO = CategoryModelSerializer(data = JDO)
        if CDO.is_valid():
            CDO.save()
            return Response({'insert':'data inserted successfully'})
        else:
            return Response(CDO.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        CO = Category.objects.get(Category_id=id)
        UCDO = CategoryModelSerializer(CO, data = request.data)
        if UCDO.is_valid():
            UCDO.save()
            return Response({'update':'data is updated succesfully'})
        else:
            return Response(UCDO.errors, status=status.HTTP_404_NOT_FOUND)
    
    def patch(self, request, id):
        CO = Category.objects.get(Category_id=id)
        UCDO = CategoryModelSerializer(CO, data = request.data, partial = True)
        if UCDO.is_valid():
            UCDO.save()
            return Response({'update':'data is updated successfully'})
        else:
            return Response(UCDO.errors, status = status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):
        Category.objects.get(Category_id = id).delete()
        return Response({'deletion':'data is deleted successfully'})
    

class ProductCrud(APIView):
    def get(self, request,id):
        PDO = Product.objects.all()
        PJO = ProductModelSerializer(PDO, many = True)
        return Response(PJO.data)
    
    def post(self,request,id):
        JDO = request.data
        PDO = ProductModelSerializer(data = JDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'insert':'data inserted successfully'})
        else:
            return Response(PDO.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        PO = Product.objects.get(id=id)
        UPDO = ProductModelSerializer(PO, data = request.data)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'update':'data is updated succesfully'})
        else:
            return Response(UPDO.errors, status=status.HTTP_404_NOT_FOUND)
    
    def patch(self, request, id):
        PO = Product.objects.get(id=id)
        UPDO = ProductModelSerializer(PO, data = request.data, partial = True)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'update':'data is updated successfully'})
        else:
            return Response(UPDO.errors, status = status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):
        Product.objects.get(id = id).delete()
        return Response({'deletion':'data is deleted successfully'})
    

