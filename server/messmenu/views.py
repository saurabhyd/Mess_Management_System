from django.shortcuts import render,HttpResponse
from .forms import messform
from .models import menu

# Create your views here.
def messmenu(request):

    if request.method == 'POST':
        form = messform(request.POST)
        if form.is_valid():
            b=form.cleaned_data['messblock']
            d=form.cleaned_data['days']
            if b!=0 and d!='zero':
                foods=menu.objects.filter(messbno=b).filter(weekday=d)
                return HttpResponse("hello" + b+ "    sdfd   " + d)
                #return render(request, 'messmenu/menu.html', {'form': form,'foods':foods,})
            #else:

    else:
        form = messform()

    return render(request, 'messmenu/menu.html',{'form':form})