from django.shortcuts import render
from rest_framework import generics
from myapp.models import Movie



class MovieAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()