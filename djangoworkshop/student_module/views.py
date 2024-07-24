from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import student_data
def first(request):
    students=student_data.objects.all()
    if request.method=='POST':
        firstname=request.POST.get('first_name'),
        lastname=request.POST.get('last_name'),
        email=request.POST.get('email'),
        gender=request.POST.get('gender'),

        student_data.objects.create(
            first_name=firstname,
            last_name=lastname,
            email=email,
            gender=gender
        
        )
    return render(request,'first.html',{'students':students})
    return HttpResponse("Data added successfully. <a href='/first'>Go back</a>")
        
    
