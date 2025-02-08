
import requests
from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .serializers import *
# Create your views here.
from rest_framework.response import Response


@api_view(['GET','POST'])
def FBV_List(request):
    if request.method=='GET':
        guest = Teacher.objects.all()
        serializer = TeacherSerializer(guest,many=True,)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED,)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def Fbv_pk(request,pk):
    
    try:
        guest = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        
        serializer = TeacherSerializer(guest)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer = TeacherSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class Teacher_list(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class Teacher_pk(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class Student_list(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class Student_pk(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class Test_list(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class Test_pk(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class Message_list(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAdminUser]

class Message_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAdminUser]

class notification_list(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Notificate.objects.all()
    serializer_class = NotificationSerializer

class notification_pk(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Notificate.objects.all()
    serializer_class = NotificationSerializer
