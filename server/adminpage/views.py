from django.shortcuts import render, redirect
from .models import messadmin
from messmenu.models import menu
from .forms import adminlogin, enterdetails


# Create your views here.
def admin(request):
    if request.method == 'POST':
        form = adminlogin(request.POST)
        if form.is_valid():
            aid = form.cleaned_data['aid']
            pw = form.cleaned_data['pw']
            user = messadmin.objects.all().filter(id=aid).filter(pwd=pw)
            if user:
                #us = messadmin.objects.get(id=aid)

                return redirect('adminlogin/'+aid)
            else:
                return render(request, 'adminpage/admin.html', {'form': form, 'message': ' Invalid Login Credentials'})
    form = adminlogin()
    return render(request, 'adminpage/admin.html', {'form': form})


def manageadmin(request,aid):
    f = enterdetails()
    us=messadmin.objects.get(pk=aid)

    if request.method == 'POST':

        form2 = enterdetails(request.POST)
        if form2.is_valid():
            d = form2.cleaned_data['days']
            typ = form2.cleaned_data['tp']
            m1 = form2.cleaned_data['fd']
            if d!='zero' and typ != 'zero':
                if typ == 'Breakfast':
                    var2 = 1
                elif typ == 'Lunch':
                    var2 = 2
                elif typ == "Dinner":
                    var2 = 3

                if d == 'Monday':
                    var1 = 1
                elif d== 'Tuesday':
                    var1 = 2
                elif d== 'Wednesday':
                    var1 = 3
                elif d== 'Thursday':
                    var1 = 4
                elif d== 'Friday':
                    var1 = 5
                elif d== 'Saturday':
                    var1 = 6
                elif d== 'Sunday':
                    var1 = 7
                administrator = messadmin.objects.get(pk=aid)
                menuvar = menu.objects.get(s1=var1,s2=var2,messbno=administrator.messbno)
                menuvar.weekday = d
                menuvar.type = typ
                menuvar.s2 = var2
                menuvar.food = m1
                menuvar.messbno = administrator.messbno
                menuvar.s1 = var1

                menuvar.save()

                return render(request,'adminpage/adminlogin.html',{'us': us, 'f': f,'message':'Menu has been updated'})
            else:
                return render(request, 'adminpage/adminlogin.html', {'us': us, 'f': form2})

    return render(request, 'adminpage/adminlogin.html',{'us':us,'f':f} )
