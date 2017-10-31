from django.shortcuts import render, HttpResponse
from .models import student_details,messreg,feed
from messmenu.models import mess

# Create your views here.

def details(request, usid):
    aval = messreg.objects.all().filter(usn=usid)
    us = student_details.objects.all().filter(usn=usid)

    if request.method == 'POST':
        selectedmess=mess.objects.get(messbno=request.POST['msb'])
        selectedmess.vacancy-=1
        selectedmess.save()

        regvar = messreg()
        regvar.messbno = selectedmess.messbno
        regvar.validity = '2017-12-03'
        regvar.usn = usid

        regvar.save()

        return render(request,'student/studentlogin.html', {'us':us,'var':3,'bno':selectedmess.messbno})

    if aval:
        aval = aval.values()
        bno=aval[0]['messbno']
        return render(request,'student/studentlogin.html', {'us':us,'var':1,'bno':bno})
    else:
        messblocks = mess.objects.all()
        return render(request, 'student/studentlogin.html', {'us': us, 'var': 2,'messblocks':messblocks})

def feedback(request,usid):


    aval = messreg.objects.all().filter(usn=usid)
    us = student_details.objects.all().filter(usn=usid)
    messblocks = mess.objects.all()
    if request.method == 'POST':
        var = feed()
        b = messreg.objects.get(usn=usid)
        var.block=b.messbno
        var.fdb=request.POST['feedtext']
        var.save()

        return render(request,'student/studentfeedback.html',{'var':1,'b':b})

    if aval:
        b = messreg.objects.get(usn=usid)
        return render(request,'student/studentfeedback.html',{'b':b})
    else:
        return render(request, 'student/studentlogin.html', {'us': us, 'var': 4,'messblocks':messblocks})