from django.shortcuts import render

# Create your views here.
def guest(request):
    return render(request, 'guestpage/guest.html')