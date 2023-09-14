from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import StackSerializer
from rest_framework.response import Response
from django.utils import timezone
import datetime
import pytz
from .models import Stack




@api_view(["GET", "POST","PUT","PATCH","DELETE"])
def StackApiView(request, pk=None, *args, **kwargs):
    method = request.method

    # if method == "GET":
    #     #add data using query_parameter
    #     name = request.GET.get('name')
    #     print(type(name))
        
    #     if name and type(name)==str :
    #       Stack.objects.create(name=name)

    #     # list view
    #     queryset = Stack.objects.all()
    #     data = StackSerializer(queryset, many=True).data
    #     return Response(data)
       
    if method == "POST":
        print(request.POST)
        serializer = StackSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            name = serializer.validated_data.get('name')  # type: ignore
            serializer.save()
            data = serializer.data
            return Response(data)
        return Response({"invalid": "not good data"}, status=400)


@api_view(["GET","PUT","PATCH","DELETE"])
def EditStackApiView(request,name_or_pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if name_or_pk is not None:
            if name_or_pk.isdigit():
                obj = get_object_or_404(Stack, pk=name_or_pk)
            else:
                obj = get_object_or_404(Stack, name=name_or_pk)
            data = StackSerializer(obj, many=False).data
            return Response(data) 
        
        

    if method == 'PUT':
        if name_or_pk is not None:
            try:
                if name_or_pk.isdigit():
                    instance = Stack.objects.get(pk=name_or_pk)
                else:
                    instance = Stack.objects.get(name=name_or_pk)
            except Stack.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            if request.method == 'PUT':
                serializer = StackSerializer(instance, data=request.data)
            else:  # PATCH request
                serializer = StackSerializer(instance, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if method == "DELETE":
        if name_or_pk is not None:
            if name_or_pk.isdigit():
                obj = get_object_or_404(Stack, pk=name_or_pk)
            else:
                obj = get_object_or_404(Stack, name=name_or_pk)

            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
     

# class StackListApiView():
#   queryset = Stack.objects.all()
#   serializer_class =  StackSerializer

#   def get(self, request, *args, **kwargs):
#     name = request.GET.get('name')
#     if name:
#      Stack.objects.create(name=name)
#     return self.list(request, *args, **kwargs)
  

# class stackEditApiView(generics.RetrieveUpdateDestroyAPIView):
#   queryset = Stack.objects.all()
#   serializer_class = StackSerializer
#   lookup_field ='pk'

#   def perform_update(self, serializer):
#         serializer.save()
        

#   def perform_destroy(self, instance):
#         super().perform_destroy(instance)
   