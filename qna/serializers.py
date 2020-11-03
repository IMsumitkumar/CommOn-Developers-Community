from rest_framework import serializers
from student_gp.models import MessageModel


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = ['id', 'date_created', 'room', 'user', 'message']
