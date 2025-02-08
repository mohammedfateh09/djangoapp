

from rest_framework import serializers

from authentication.serializers import UserSerializer
# from .models import User
from .models import *

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer() 
    class Meta:
        model = Teacher
        fields = ['id', 'lessonurl', 'timelesson', 'user']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    # user = UserSerializer() 
    class Meta:
        model = Message
        fields = '__all__' 

class NotificationSerializer(serializers.ModelSerializer):
    # user = UserSerializer() 
    class Meta:
        model = Notificate
        fields = '__all__'