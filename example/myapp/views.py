from django.shortcuts import render
from myapp.models import Data
from myapp.models import Readonly
from myapp.serializers import DataSerializer
from myapp.serializers import ReadonlySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import logging
logger = logging.getLogger(__name__)

class DataList(APIView):
    def get(self, request, format=None):
        datas = Data.objects.all()
        serializer = DataSerializer(datas, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = DataSerializer(data=request.data)
        dic = {
            'body': '/echo ' + request.data['text'],
            'connectColor': '#FFFFFF',
            'connectInfo': [{
                'title': '이름',
                'description': request.data['writerName'],
            }],
        }
        if serializer.is_valid():
            serializer.save()
            return Response(dic, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Readonly(APIView):
    def get(self, request, format=None):
        readonly = Readonly.objects.all()
        serializer = ReadonlySerializer(readonly, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReadonlySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)