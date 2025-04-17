from rest_framework import viewsets
from .models import Employee, User
from .serializers import EmployeeSerializer, UserSerializer
from django.http import JsonResponse
from django.core.serializers import serialize
import json

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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