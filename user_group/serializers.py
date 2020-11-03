from rest_framework import serializers
from user_group.models import CreateGroup


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateGroup
        fields = '__all__'
