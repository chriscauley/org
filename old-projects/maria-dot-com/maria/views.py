from django.template.response import TemplateResponse
import grappelli

def home(request):
  return TemplateResponse(request,'home.html',{})
