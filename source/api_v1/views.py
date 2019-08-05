from webapp.models import New
from rest_framework import viewsets
from api_v1.serializers import NewSerializer


class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer

