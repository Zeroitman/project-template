from webapp.models import New
from rest_framework import serializers


class NewSerializer(serializers.ModelSerializer):

    class Meta:
        model = New
        fields = ('name', 'text')
