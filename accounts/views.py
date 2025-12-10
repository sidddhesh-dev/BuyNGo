from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializer import UserSerializer, RegisterSerializer
from django.shortcuts import render

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "User created successfully"})
        return Response(serializer.errors, status=400)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user   # logged in user
        serializer = UserSerializer(user)
        return Response(serializer.data)

def accounts(request):
    return render(request,'account/accounts.html')
