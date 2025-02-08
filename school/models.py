import random
import string
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from authentication.models import User

attend_type= ( ('1','1'),('0','0'),('2','2'))

class Teacher(models.Model):
    user = models.OneToOneField(User,related_name='job_owner',on_delete=models.CASCADE)
    lessonurl = models.CharField(max_length=50,blank=True,null=True)
    timelesson = models.CharField(max_length=10,blank=True,null=True)
    def __str__(self):
        return self.user.first_name

class Student(models.Model):
    # user = models.OneToOneField(User,related_name='student_owner',on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    name = models.CharField(max_length=25,blank=True,null=True)
    father = models.CharField(max_length=20,blank=True,null=True)
    birth_place = models.CharField(max_length=20,blank=True,null=True)
    birth_date = models.DateField(blank=True,null=True)
    place = models.CharField(max_length=20,blank=True,null=True)
    phone = models.CharField(max_length=15,blank=True,null=True)
    level = models.name = models.CharField(max_length=15,blank=True,null=True)
   
    def __str__(self):
        return self.user.first_name 

    
    # def save(self, *args, **kwargs):
    #     if self.user_id:  # If no user is assigned, create one
    #         random_username = "st" + ''.join(random.choices(string.digits, k=6))
    #         random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    #         user = User.objects.create_user(
    #             username=random_username,
    #             password=random_password,
    #             is_staff=True,
    #             role = 'student',
    #             is_superuser=False,
    #             first_name=self.name,
    #             last_name=self.father
    #         ) 
    #         self.user = user  # Assign the newly created user to the student
    #     super().save(*args, **kwargs) 

class Level(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Notificate(models.Model):  
    # sender = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="sent_notification")
    message = models.TextField()
    is_sent = models.BooleanField(default=False)  # To track notifications
    read = models.BooleanField(default=False)  # To track notifications
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.student.name}"
    
class Test(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    title = models.CharField( max_length=50)
    marks = models.CharField(max_length=50)
    note = models.TextField(max_length=50)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.student.name}"
    
@receiver(post_save, sender=Test)
def create_notification_on_high_marks(sender, instance, created, **kwargs):
    if created and int(instance.marks) > 80:  # Check if marks > 80
        Notificate.objects.create(
            message=f"{instance.student.name} اختبر {instance.marks} في {instance.title}",
            is_sent=True,  # Mark as sent
            read=False
        )
        print('Notification sent successfully!')
    
# @receiver(post_save, sender=Test)
# def create_notification(sender, instance, created, **kwargs):
#     if created:  # Only notify when a new test is added
#         Notificate.objects.create(
#             sender=instance.teacher.user,  # Assuming `Test` has a `teacher` field
#             message=f"New test added: {instance.subject} - {instance.marks} marks",
#             is_sent=False,
#             read=False
#         )
    

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"From {self.sender} to {self.recipient}"
        
class Attends(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    attend = models.CharField(max_length=5)
    note = models.TextField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.attend

       
# Create your models here.
