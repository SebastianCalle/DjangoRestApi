from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from api.views import CreateUserAPIView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('api/', include('api.urls')),
    url('api-token-auth/', obtain_jwt_token),
    url('register/', CreateUserAPIView.as_view()),

]
