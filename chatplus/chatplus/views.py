from dj_rest_auth.registration.views import VerifyEmailView
from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response

class CustomVerifyEmailView(VerifyEmailView):
    def get(self, request, *args, **kwargs):
        key = kwargs.get('key')
        email_confirmation = self.get_object()
        email_confirmation.confirm(self.request)
        return redirect('http://localhost:4200') 

    def post(self, request, *args, **kwargs):
        key = request.data.get('key', '')
        email_confirmation = self.get_object()
        if email_confirmation.confirm(request):
            return Response({'detail': 'Email has been successfully verified.'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid verification key.'}, status=status.HTTP_400_BAD_REQUEST)
