from django.shortcuts import render, redirect
from .forms import FluttForm, SearchForm
from .models import Flutt
# Create your views here.

def timeline(request):
    """
    produce timeline of flutts
    :param request:
    :return:
    """
    all_of_em = Flutt.objects.order_by('created')[:10]

    search_form = SearchForm()
    create_form = FluttForm()
    context = {
        'flutts':all_of_em,
        'search_form':search_form,
        'create_form':create_form
        }

    return render(request, "timeline.html", context)

def create_flutt(request):
    """
    view for creating a new flutt
    :param request:
    :return:
    """

    if request.method == 'POST':
        form = FluttForm(request.POST)

        if form.is_valid():
            flutt = form.save(commit=False)
            flutt.save()
            return redirect('/')
        else:
            context = {'form':form}
            return render(request, "create_flutt.html", context)

    elif request.method == 'GET':

        form = FluttForm()
        context = {'form': form}

        return render(request, "create_flutt.html", context)


def search_flutts(request):
    """
    view for searching flutts
    :param request:
    :return:
    """
    if request.method == 'GET':
        q = request.GET['query_text']
        matches = Flutt.objects.filter(body__icontains=q)
        search_form = SearchForm(request.GET)
        context = {
            'flutts': matches,
            'search_form':search_form
            }
        return render(request, "timeline.html", context)


