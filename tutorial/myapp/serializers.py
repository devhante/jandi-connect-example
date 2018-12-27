from myapp.models import Data
from rest_framework import serializers


class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ('token', 'teamName', 'roomName', 'writerName', 'text', 'keyword', 'createdAt')

        