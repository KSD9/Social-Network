


from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    re_path('api/(?P<version>(v1|v2))/', include('social.urls'))
    # path('', include('social.urls')),
]
