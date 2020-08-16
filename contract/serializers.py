from rest_framework.serializers import ModelSerializer
from contract.models import Client, Request


class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        depth = 1
        fields = '__all__'


class RequestSerializer(ModelSerializer):
    client = ClientSerializer

    class Meta:
        model = Request
        fields = '__all__'

    def create(self, validated_data):
        client = validated_data.pop('client')
        return Request.objects.create(client=client, **validated_data)
