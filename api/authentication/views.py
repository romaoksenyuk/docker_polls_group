import settings

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import (ListAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView,
                                     RetrieveAPIView,
                                     CreateAPIView)
from rest_framework.response import Response

from .serializers import (
    UserSerializer, 
    FindUserSerializer,
    StudentSerializer, 
    TeacherSerializer, 
    CreateUserSerializer,
    LoginUserSerializer,)

from .models import Student, Teacher

User = get_user_model()

class FindUserAPIView(RetrieveAPIView):
    lookup_field = 'email'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class CreateUserAPIView(CreateAPIView):
    """
    Create user
    """
    # Allow any user (authenticated or not) to access this url
    permission_classes = (AllowAny,)
    serializer_class = CreateUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        
        return Response(
            data={"success": "User '{}' created successfully".format(str(user_saved))},
            status=status.HTTP_201_CREATED)

class LoginUserAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginUserSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        
        if(serializer.is_valid(raise_exception=True)):
            new_data = serializer.data
            return Response(new_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentListAPIView(ListAPIView):
    """
    All students in db (for test)
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminUser]

class TeacherListAPIView(ListAPIView):
    """
    All teachers in db (for test)
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminUser]


class UpdateUserAPIView(UpdateAPIView):
    """
    Update User
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def put(self, request):

        serializer = self.serializer_class(request.user,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteUserAPIView(DestroyAPIView):
    """
    Delete User
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def post(self, request):

        serializer = self.serializer_class(request.user,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.delete(request)

        return Response({'Status':'OK'},status=status.HTTP_200_OK)
