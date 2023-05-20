
from django.contrib import admin
from django.urls import path, include
from task import urls as task_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('backend/v1/', include(task_urls, namespace='task'))
]
