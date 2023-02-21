from django.http import JsonResponse, HttpResponse

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import Timeline
from .serializers.serializers import TimelineSerializer


@api_view(['GET', 'POST'])
def timeline_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Timeline.objects.all()
        serializer = TimelineSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = TimelineSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def timeline_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code timeline.
    """
    try:
        timeline = Timeline.objects.get(pk=pk)
    except Timeline.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TimelineSerializer(timeline)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TimelineSerializer(timeline, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        timeline.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
