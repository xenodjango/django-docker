from rest_framework.serializers import ModelSerializer
from todo_app.todo.models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
