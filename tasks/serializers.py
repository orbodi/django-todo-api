from rest_framework import serializers  
from .models import TaskModel  
  
  
class TaskSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = TaskModel  
        fields = ["id",  "title", "content", "createdAt", "updatedAt"]
        extra_kwargs = {
            "createdAt": {"read_only": True},
            "createdAt": {"read_only": True},
        }