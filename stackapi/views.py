from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import StackSerializer
from rest_framework.response import Response
from django.utils import timezone
import datetime
import pytz
from .models import Stack


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def StackApiView(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        # Handle GET request logic here
        queryset = Stack.objects.all()
        data = StackSerializer(queryset, many=True).data
        return Response(data)

    if method == "POST":
        serializer = StackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def EditStackApiView(request, name_or_pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if name_or_pk is not None:
            try:
                if name_or_pk.isdigit():
                    obj = get_object_or_404(Stack, pk=name_or_pk)
                else:
                    obj = get_object_or_404(Stack, name=name_or_pk)
                data = StackSerializer(obj, many=False).data
                return Response(data)
            except Stack.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    if method in ["PUT", "PATCH"]:
        if name_or_pk is not None:
            try:
                if name_or_pk.isdigit():
                    instance = get_object_or_404(Stack, pk=name_or_pk)
                else:
                    instance = get_object_or_404(Stack, name=name_or_pk)
            except Stack.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = StackSerializer(
                instance, data=request.data, partial=method == "PATCH")

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if method == "DELETE":
        if name_or_pk is not None:
            try:
                if name_or_pk.isdigit():
                    obj = get_object_or_404(Stack, pk=name_or_pk)
                else:
                    obj = get_object_or_404(Stack, name=name_or_pk)
                obj.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Stack.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
