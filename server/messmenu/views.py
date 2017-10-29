from django.shortcuts import render, HttpResponse
from django.db.models.query import QuerySet
from .forms import messform
from .models import menu


# Create your views here.
def messmenu(request):
    if request.method == 'POST':
        form = messform(request.POST)
        if form.is_valid():
            b = form.cleaned_data['messblock']
            d = form.cleaned_data['days']
            if b != 0:
                if d != 'zero':
                    query = menu.objects.all().filter(messbno=b).filter(weekday=d).query
                    query.order_by = ['s2']
                    foods = QuerySet(query = query, model=menu)
                    return render(request, 'messmenu/menu.html', {'form': form, 'foods': foods, })
                else:
                    query = menu.objects.all().filter(messbno=b).query
                    query.order_by = ['s1','s2']
                    foods = QuerySet(query = query, model=menu)
                    return render(request, 'messmenu/menu.html', {'form': form, 'foods': foods, })

    else:
        form = messform()

    return render(request, 'messmenu/menu.html', {'form': form})
