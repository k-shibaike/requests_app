from django.shortcuts import render
from django.http import HttpResponse



def index(request):
  return render(request, 'request/index.html')

def detail(request):
  if 'post' in request.method.lower():
        city_number = request.POST.get('location')
        print("city_number->", city_number)

        # ここにweatherAPIの処理書いてもいい

  return render(request, 'request/detail.html')