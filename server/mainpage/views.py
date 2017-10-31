from django.shortcuts import render, HttpResponse
from student.models import student_details
from student.forms import studentlogin


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = studentlogin(request.POST)
        if form.is_valid():
            us = form.cleaned_data['us']
            pw = form.cleaned_data['pw']
            user = student_details.objects.all().filter(usn=us).filter(pwd=pw)
            if user:
                return render(request, 'mainpage/index.html', {'form': form})
            else:
                return render(request, 'mainpage/index.html', {'form': form, 'message': ' Invalid login credentials'})
    form = studentlogin()
    return render(request, 'mainpage/index.html', {'form':form})
