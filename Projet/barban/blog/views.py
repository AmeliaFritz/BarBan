from django.http import HttpResponse
from django.shortcuts import render

#-*- coding: utf-8 -*-

def home(request):
    return render(request, 'blog/home.html.twig')

def boutique(request):
    return render(request, 'blog/boutique.html.twig')

def panier(request):
    return render(request, 'blog/panier.html.twig')
