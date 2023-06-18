from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import ToDoItem
from .serializers import ToDoItemSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ToDoItemListCreateView(generics.ListCreateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ToDoItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


