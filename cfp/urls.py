from django.conf.urls import url, include
from django.contrib import admin
from api.views import CreateUserAPIView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('api/', include('api.urls')),
    url('register', CreateUserAPIView.as_view()),
    url('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
