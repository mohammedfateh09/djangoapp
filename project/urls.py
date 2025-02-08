
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('school/', include('school.urls')),
    path('api-auth', include('rest_framework.urls')),
    # path('api/auth/login/', views.UserLoginView.as_view(), name='user-login'),

]


urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)