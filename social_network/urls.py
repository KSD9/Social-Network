


from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_jwt_token, name='create-token'),
    path('', include('social.urls')),

]
