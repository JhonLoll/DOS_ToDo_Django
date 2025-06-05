from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/v1/', include('myApp.urls')),
    path('admin/', admin.site.urls),
    path('tarefas/', include('myApp.urls')),
]
