from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from .models import *
from .serializers import *
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from django.contrib.auth import authenticate

# Create your views here.

@api_view(['GET'])
def root(request):
    """
    Function based root api view
    """
    return Response(
        {
            'status':status.HTTP_200_OK,
            'message': 'Task App'
        }
    )

class LoginView(APIView):
    def post(self, request):
        username = self.request.data.get('username')
        password = self.request.data.get('password')

        user = authenticate(username=username, password = password)

        if user:
            access = AccessToken.for_user(user)
            refresh = RefreshToken.for_user(user)

            return Response({
                'status' : status.HTTP_200_OK,
                'access': str(access),
                'refresh': str(refresh),
            })
        else:
            return Response({
                'status' : status.HTTP_400_BAD_REQUEST,
                'message': 'Invalid Credentials',
            })

# class LogoutView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     def post(self, request):
#            rtoken = request.data["refresh_token"]
#            token = RefreshToken(rtoken)
#            token.blacklist()
#            return Response(status=status.HTTP_205_RESET_CONTENT)
    
class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

class GetTaskList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def list(self, request):
        tasks = Task.objects.filter(assigned_user = request.user).all()
        serializer = TaskSerializer(tasks, many=True)
        return Response({
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })
    
class GetTaskDetail(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]