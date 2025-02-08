from django.urls import include, path
from authentication import views
app_name='authentication'

# router = DefaultRouter()
# router.register(r'users', views.UserViewSet)

# router = DefaultRouter()
# router.register('teacher',views.viewsets_guest)
# router.register('movie',views.viewsets_movie)
# router.register('reservation',views.viewsets_reservation)

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('logout/', views.UserLogoutView.as_view(), name='user-logout'),
    path('users/', views.User_list.as_view(), name='user'),
    path('users/<int:pk>', views.User_pk.as_view(), name='user-pk'),

  

]
