from rest_framework import viewsets
from .models import Employee, User, Tarea, Place, Excusa, Maintenance
from .serializers import EmployeeSerializer, UserSerializer, TareaSerializer, PlaceSerializer, ExcusaSerializer, MaintenanceSerializer
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class= TareaSerializer

class ExcusaViewSet(viewsets.ModelViewSet):
    queryset = Excusa.objects.all()
    serializer_class = ExcusaSerializer

class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer

def get_employees(request):
    employees = Employee.objects.select_related('user').all()
    data = [
        {
            "id": emp.id,
            "role": emp.role,
            "user": {
                "id": emp.user.id,
                "name": emp.user.name,
                "email": emp.user.email,
                "phone": emp.user.phone
            }
        }
        for emp in employees
    ]
    return JsonResponse(data, safe=False)



@api_view(['GET'])
def get_tasks_by_employee(request, employee_id):
    tasks = Tarea.objects.filter(employee__id=employee_id).select_related('employee__user')
    serializer = TareaSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_excusas_by_employee(request, employee_id):
    excusa = Excusa.objects.filter(employee__id=employee_id).select_related('employee__user')
    serializer = ExcusaSerializer(excusa, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_maintenances(request):
    mantenimiento = Maintenance.objects.all()
    serializer = MaintenanceSerializer(mantenimiento, many=True)
    return Response(serializer.data)