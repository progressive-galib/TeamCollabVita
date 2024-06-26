from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProjectViewSet, TaskViewSet, CommentViewSet, UtilsViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'projects/(?P<project_id>[^/.]+)/tasks', TaskViewSet, basename='task')
router.register(r'projects/(?P<project_id>[^/.]+)/tasks/(?P<task_id>[^/.]+)/comments', CommentViewSet, basename='comment')
router.register(r'utils', UtilsViewSet, basename='utils')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
