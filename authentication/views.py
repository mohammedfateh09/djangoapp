
from authentication.serializers import UserSerializer
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# from school.permissions import IsAdmin

from rest_framework import generics,mixins
from .models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from school.models import Teacher,Student

class UserRegistrationView(APIView):
    def post(self, request):
        # print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    @receiver(post_save,sender=User)
    def create_teacher(sender,instance,created,**kwargs):
        if created: 
            if instance.role=='teacher':     
                Teacher.objects.create(user = instance)
                
  



class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            if created:
                token.delete()  # Delete the token if it was already created
                token = Token.objects.create(user=user)

            return Response({'token': token.key,
                              'username': user.username,
                                'role': user.role,
                                'id':user.pk,
                                'first_name':user.first_name,
                                'is_staff':user.is_staff,
                                'is_superuser':user.is_superuser,
                                'last_name':user.last_name,
                             
                                })
        else:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)



class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.headers) 
        token_key = request.auth.key
        token = Token.objects.get(key=token_key)
        token.delete()
        return Response({'detail': 'Successfully logged out.'})
    
class User_list(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class User_pk(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

