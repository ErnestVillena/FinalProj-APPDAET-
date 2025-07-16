from django.shortcuts import render
from django.views.generic.list import ListView
from .models import IdType, IdCredentials, IdAttachment

# Create your views here.
class IdList(ListView):
    model = IdType
    context_object_name = 'ids'