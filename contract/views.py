from rest_framework.decorators import api_view
from rest_framework.response import Response
from contract.models import Client, Request
from contract.serializers import ClientSerializer, RequestSerializer


@api_view(['GET', 'POST'])
def client_list(request):
    if request.method == 'GET':
        items = Client.objects.order_by('pk')
        serializer = ClientSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request, pk):
    try:
        item = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ClientSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClientSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def request_list(request):
    if request.method == 'GET':
        items = Request.objects.order_by('pk')
        serializer = RequestSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def request_detail(request, pk):
    try:
        item = Request.objects.get(pk=pk)
    except Request.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = RequestSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RequestSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)
