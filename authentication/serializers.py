

from rest_framework import serializers
from .models import User


from school.models import Teacher
# from school.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['id','username', 'email', 'role', 'password','first_name','is_staff',
                  'is_superuser','last_name','image','b_date',
                  'phone','state','city','gender']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

        
    
