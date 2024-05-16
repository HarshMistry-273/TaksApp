from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class TaskSerializer(serializers.ModelSerializer):
    assigned_user = serializers.PrimaryKeyRelatedField(queryset = User.objects.exclude(is_staff = True), source = 'assigned_user.username')
    tid = serializers.ReadOnlyField()
    class Meta:
        model = Task
        exclude = ['created_at', 'updated_at']
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args,  **kwargs)
    #     user = self.context['request'].user
    #     if not user.is_staff:
    #         self.Meta.exclude += ['title','description','due_date','priority']
    #     elif user.is_staff:
    #         self.Meta.exclude += ['created_at', 'updated_at']


    def update(self, insatnce,validated_data):
        if not self.context['request'].user.is_staff:
            insatnce.status = validated_data.get('status', insatnce.status)
        return insatnce



