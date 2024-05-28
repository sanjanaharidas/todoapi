from django.shortcuts import render
from task.models import Task
from task.serializers import TaskSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from task.serializers import UserSerializer
# Create your views here.
class AllTasks(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer

class NotcompletedTasks(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class = TaskSerializer
    def get_queryset(self):
        qs=self.queryset
        queryset=qs.filter(completed=False)
        return queryset

class CompletedTasks(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        qs = self.queryset
        queryset = qs.filter(completed=True)
        return queryset

class CreateUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
