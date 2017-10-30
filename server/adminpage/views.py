from django.shortcuts import render
from .models import messadmin
from .forms import adminlogin

# Create your views here.
def admin(request):
    if request.method == 'POST':
        form = adminlogin(request.POST)
        if form.is_valid():
            aid = form.cleaned_data['aid']
            pw = form.cleaned_data['pw']
            user = messadmin.objects.all().filter(id=aid).filter(pwd=pw)
            if user:
                return render(request, 'adminpage/admin.html', {'form': form})
            else:
                return render(request, 'adminpage/admin.html', {'form': form, 'message':'Invalid Login Credentials'})
    form = adminlogin()
    return render(request,'adminpage/admin.html', {'form':form})