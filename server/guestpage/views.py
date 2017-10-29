from django.shortcuts import render,HttpResponse
from .forms import guestform
from .models import guestreg

# Create your views here.
def guest(request):

    if request.method == 'POST':
        form = guestform(request.POST)
        if form.is_valid():
            #if form.block!=0 and form.meal!='zero':
            form.save()
            return HttpResponse('<div class="alert alert-success"><strong>Success!</strong> Your Meal has been Booked</div>')
            #else:
                #return render(request, 'guestpage/guest.html', {'form': form})
    form=guestform()
    return render(request, 'guestpage/guest.html', {'form':form})