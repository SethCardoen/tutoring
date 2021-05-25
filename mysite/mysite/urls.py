from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('basesite/', include('basesite.urls')),
    path('admin/', admin.site.urls),
]