from django.shortcuts import render
from myapp.models import Data
from myapp.serializers import DataSerializer
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
            'body': request.data['text'],
            'connectColor': '#FFFFFF',
            'connectInfo': [{
                'title': '이름',
                'description': request.data['writerName'],
            }],
        }
        if serializer.is_valid():
            serializer.save()
            return Response(dic, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
