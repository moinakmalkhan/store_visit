from rest_framework import serializers
from .models import Employee, Store, Visit

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'phone_number']

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'employee']

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['id', 'date_time', 'store', 'latitude', 'longitude']

    def validate(self, attrs):
        attrs['employee'] = self.context['request'].employee
        return attrs
