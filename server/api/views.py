from django.shortcuts import render

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt



def index(request):
#    response = User.objects.all()
   response ='hello dummy text'
   return HttpResponse(response)

# Create your views here.
