from rest_framework import serializers
from task.models import Task
from django.contrib.auth.models import User
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=['id','task_name','task_desc','date_added','completed']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','username','password']


    def create(self, validated_data):#after validation
        u=User.objects.create_user(username=validated_data['username'],password=validated_data['password'])
        u.save()
        return u
