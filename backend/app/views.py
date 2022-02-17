from django.shortcuts import render
from django.http import JsonResponse


def test(request):
    return JsonResponse({"mousa":"mousa nageh "})

# Create your views here.
