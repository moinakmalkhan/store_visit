from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import Employee

class PhoneAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Phone '):
            return None

        phone_number = auth_header.split(' ')[1]

        try:
            employee = Employee.objects.get(phone_number=phone_number)
        except Employee.DoesNotExist:
            raise AuthenticationFailed('No such employee')
        request.employee = employee
        return (None, None)
