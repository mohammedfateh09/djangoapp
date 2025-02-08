from django.urls import include, path
from school import views

app_name='school'

urlpatterns = [
    path('teacher/', views.Teacher_list.as_view()),
    path('teachers/', views.Teacher_list.as_view()),

    path('teacher/<int:pk>', views.Teacher_pk.as_view()),
    # test
    path('test/', views.Test_list.as_view()),
    path('test/<int:pk>', views.Test_pk.as_view()),

        # teacher
    path('student/', views.Student_list.as_view()),
    path('student/<int:pk>', views.Student_pk.as_view()),
    path('message/', views.Message_list.as_view()),
    path('message/<int:pk>', views.Message_pk.as_view()),
    path('notifi/', views.notification_list.as_view()),
    path('notifi/<int:pk>', views.notification_pk.as_view()),
    # path('notifications/', views.get_notifications),
]
