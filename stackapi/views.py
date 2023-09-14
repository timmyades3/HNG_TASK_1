from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import PersonSerializer
from rest_framework.response import Response
from django.utils import timezone
import datetime
import pytz
from .models import Person


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def PersonApiView(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        # Handle GET request logic here
        queryset = Person.objects.all()
        data = PersonSerializer(queryset, many=True).data
        return Response(data)

    if method == "POST":
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def EditPersonApiView(request, name_or_pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if name_or_pk is not None:
            try:
                if name_or_pk.isdigit():
                    obj = get_object_or_404(Person, pk=name_or_pk)
                else:
                    obj = get_object_or_404(Person, name=name_or_pk)
                data = PersonSerializer(obj, many=False).data
                return Response(data)
            except Person.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    if method in ["PUT", "PATCH"]:
        if name_or_pk is not None:
            try:
                if name_or_pk.isdigit():
                    instance = get_object_or_404(Person, pk=name_or_pk)
                else:
                    instance = get_object_or_404(Person, name=name_or_pk)
            except Person.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = PersonSerializer(
                instance, data=request.data, partial=method == "PATCH")

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if method == "DELETE":
        if name_or_pk is not None:
            try:
                if name_or_pk.isdigit():
                    obj = get_object_or_404(Person, pk=name_or_pk)
                else:
                    obj = get_object_or_404(Person, name=name_or_pk)
                obj.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Person.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
