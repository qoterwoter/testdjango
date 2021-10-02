from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from .models import  *
from .serializers import *
from rest_framework.authentication import TokenAuthentication,SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import viewsets;

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def index(request):
    drivers = Drivers.objects.all()
    driversPhoto = DriversPhoto.objects.all()
    return render(request, 'main/index.html', {'drivers':drivers,'photos': driversPhoto})

def about(request):
    return render(request, 'about/about.html')

def landing(request):
    return render(request, 'landing/landing.html')

def admin(request):
    return render(request, "/admin")

def projects(request):
    return render(request,'/projects')

class UserView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, forman=None):
        content = {
            'user' : str(request.user),
            'auth' : str(request.auth),
        }
        return Response(content)
@api_view(['GET','POST'])
def drivers_list(request):
    if request.method == 'GET':
        drivers = Drivers.objects.all()
        serializer = DriversSerializer(drivers, many=True)
        authentication_classes = [TokenAuthentication, ]
        permission_classes = [IsAuthenticated, ]
        return JsonResponse({"data": serializer.data})

    elif request.method == 'POST':
        serializer = DriversSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def drivers_detail(request,id):
    try:
        student = Drivers.objects.get(id=id)
    except Drivers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DriversSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DriversSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def news_list(request):
    if request.method == 'GET':
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        authentication_classes = [TokenAuthentication, ]
        permission_classes = [IsAuthenticated, ]
        return JsonResponse({"data": serializer.data})

    elif request.method == 'POST':
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectsView(APIView):
    def get(self, request):
        ProjectsApi = Projects.objects.all()
        serializer = ProjectsSerializer(ProjectsApi, many=True)
        return JsonResponse({"Projects": serializer.data})

    def post(self, request):
        ProjectsApi = request.data.get('Projects')
        serializer = ProjectsSerializer(data=ProjectsApi)
        if serializer.is_valid(raise_exception=True):
            employee_saved = serializer.save()
        return Response({"success": "Employee '{}' created successfully".format(employee_saved.name)})
