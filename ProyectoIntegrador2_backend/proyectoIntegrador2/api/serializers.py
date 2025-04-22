from rest_framework import serializers
from .models import Employee, User, Place, Tarea, Excusa, Maintenance

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()   
    class Meta:
        model = Employee
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

class TareaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tarea
        fields = '__all__'

class ExcusaSerializer(serializers.ModelSerializer):


    class Meta:
        model = Excusa
        fields = '__all__'

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'