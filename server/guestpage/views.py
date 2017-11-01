from django.shortcuts import render, HttpResponse
from .forms import guestform
from django.utils.datetime_safe import date


def guest(request):
    if request.method == 'POST':
        form = guestform(request.POST)
        if form.is_valid():
            ml = form.cleaned_data['meal']
            dt = form.cleaned_data['date']
            if ml !='zero' and dt >= date.today():
                form.save()
                form = guestform()
                return render(request, 'guestpage/guest.html',
                              {'form': form, 'var': 1})

            else:
                return render(request, 'guestpage/guest.html',
                              {'form': form, 'var' : 2})

    form = guestform()
    return render(request, 'guestpage/guest.html', {'form': form})
