from myapp.models import Data
from myapp.models import Echo
from rest_framework import serializers


class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ('token', 'teamName', 'roomName', 'writerName', 'text', 'keyword', 'createdAt')

class EchoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Echo
        fields = ('token', 'teamName', 'roomName', 'writerName', 'text', 'keyword', 'createdAt')