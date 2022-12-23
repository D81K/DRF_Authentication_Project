from django.shortcuts import render , HttpResponse , get_object_or_404
from .models import Student

from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins, viewsets
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from .pagination import MyCursorPagination, MyLimitOffsetPagination, SmallPageNumberPagination, LargePageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.permissions import ( 
    IsAuthenticated, 
    AllowAny,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    DjangoModelPermissions,
    )


def home(request):
    return HttpResponse('<h1> API PAGE </h1>')

#function based views

# @api_view(['GET','POST'])
# def student_api(request):
#     if request.method == 'GET':
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = StudentSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 "message" : "Student Created!"
#             }
#             return Response(data, status= status.HTTP_201_CREATED)
#         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

# class StudentList(APIView):
    
#     def get(self, request):
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = StudentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)

class StudentMVS(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # pagination_class = LargePageNumberPagination
    # pagination_class = MyLimitOffsetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['first_name','last_name']
    search_fields = ['first_name']
    ordering_fields = ['number', 'last_name']

    permission_classes = [DjangoModelPermissions]
