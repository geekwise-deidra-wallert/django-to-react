from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from todo.serializers import TodoSerializer, UserSerializer, GroupSerializer
from .models import Todo

class TodoViewSet (viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class UserViewSet ( viewsets.ReadOnlyModelViewSet ):
    """
        API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet ( viewsets.ReadOnlyModelViewSet ):
    """
        API endpoint that allows users to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer