from functools import partial
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializers
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST','PUT'])
def Student_list(request):
    if request.method=='GET':
        stu=Student.objects.all()
        serializer=StudentSerializers(stu,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    if request.method=='PUT':
        id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializers(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        