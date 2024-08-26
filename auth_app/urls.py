from auth_app.views import CustomUserViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
