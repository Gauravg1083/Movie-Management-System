from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie,Student,Slides
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import MovieSerializer
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
from .forms import StudentForm,MovieForm


def movie_list(request):
    movie = Movie.objects.all()
    if request.method =='GET':
        st = request.GET.get('searchname')
        if st !=None:
            movie = Movie.objects.filter(name__icontains=st)
    return render(request,'movielist.html',{'movie':movie})

def add_movie(request):
    form = MovieForm
    if request.method =='POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render (request,'addmovie.html',{'form':form})

# class MovieViewset(viewsets.ModelViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     throttle_classes = [AnonRateThrottle]
#
#
# @api_view(['GET','POST'])
# def movie_data(request):
#
#     if request.method =='GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies,many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET','PUT','DELETE'])
# def movie_detail(request, pk):
#
#     if request.method == 'GET':
#         movie=Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.dalete()
#         return Response('data has been deleted successfully')
#

def student_list(request):
    data = Student.objects.all()
    return render(request,'studentlist.html',{'data':data})


def AddStudent(request):
    form = StudentForm
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/student-list")
    return render(request,'addstudent.html',{'form':form})

def update_movie(request,id):
    movie  = Movie.object.get(id=id)
    form = MovieForm(instance=movie)
    if request =='POST':
        form = MovieForm(request.Post,instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/movie')
    return render(request,'updatemovie.html',{'form':form})

def delete_movie(request,id):
    movie = Movie.object.filter(id=id).delete()
    return redirect('/')

def SlidesPage(request):
    sld = Slides.objects.all()
    return render(request,'Slides.html',{'sld':sld})

def movie_detail(request,id):
    movie = get_object_or_404(Movie,pk=id)
    return render(request,'moviedetail.html',{'movie':movie})