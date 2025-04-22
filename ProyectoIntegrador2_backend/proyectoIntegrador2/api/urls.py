from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, UserViewSet, get_employees, get_tasks_by_employee, TareaViewSet, PlaceViewSet, ExcusaViewSet, get_excusas_by_employee, MaintenanceViewSet, get_maintenances

router = DefaultRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'users', UserViewSet )
router.register(r'tareas', TareaViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'excusas', ExcusaViewSet)
router.register(r'maintenances', MaintenanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('employees/', get_employees, name='get_employees'),
    path('tasks/employee/<int:employee_id>/', get_tasks_by_employee, name='get_tasks_by_employee'),
    path('excusa/employee/<int:employee_id>/', get_excusas_by_employee, name='get_excusas_by_employee'),
    path('mantenimientos/', get_maintenances, name='get_maintenances')

]
