from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class UserListAPI(APIView):
    def get(self, request):
        users = User.objects.all().values('id', 'username', 'email')
        return Response(users, status=status.HTTP_200_OK)

class UserDetailAPI(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.values('id', 'username', 'email').get(pk=pk)
            return Response(user, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
