from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todo_app.views import TodoViewSet

router = DefaultRouter()
router.register('todos', TodoViewSet, basename='todos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
