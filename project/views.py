from django.shortcuts import render

# Create your views here.
def Page1(request):
  return render(request,'pages/page1.html')