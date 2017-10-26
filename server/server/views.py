from django.shortcuts import redirect

def gohome(request):
    return redirect('/mainpage')