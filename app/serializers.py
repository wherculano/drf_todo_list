from .models import ToDo

from rest_framework.serializers import ModelSerializer


class ToDoSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
