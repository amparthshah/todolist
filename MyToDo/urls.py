from django.contrib import admin
from django.urls import path
from django.urls.conf import include


admin.site.site_header = "ToDoList By Parth Shah"
admin.site.site_title = "ToDoList"
admin.site.index_title = "ToDoList"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ToDoApp.urls')),
]
