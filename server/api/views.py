from django.shortcuts import render

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt



def index(request):
#    response = User.objects.all()
   response =request.method
   return HttpResponse(response)

# Create your views here.

@csrf_exempt 
def lda(request):
   if request.method == 'POST':
      response = 'reply from a successfull post request'
      temp = request.body
      # ans = analysisDecision(temp)
      return HttpResponse(response) 
   return HttpResponse('else response')
