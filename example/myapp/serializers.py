from myapp.models import Data
from myapp.models import Readonly
from rest_framework import serializers


class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ('token', 'teamName', 'roomName', 'writerName', 'text', 'keyword', 'createdAt')

class ReadonlySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Readonly
        fields = ('token', 'teamName', 'roomName', 'writerName', 'text', 'keyword', 'createdAt')