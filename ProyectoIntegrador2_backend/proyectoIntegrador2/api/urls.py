from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, UserViewSet, get_employees

router = DefaultRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'users', UserViewSet )

urlpatterns = [
    path('', include(router.urls)),
    path('employees/', get_employees, name='get_employees'),
]
