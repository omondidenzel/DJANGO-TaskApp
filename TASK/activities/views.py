from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse

class AddList(forms.Form):
    task = forms.CharField(label='Task', max_length=100)

#task_list = []

# Create your views here.
def index(request):
    if "task" not in request.session:
        request.session['task'] = []

    #return HttpResponse('working')
    return render(request, "activities/index.html", {'lol':request.session['task']})

def add(request):
    if request.method == 'POST':
        form = AddList(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            request.session['task'] += [task]
            return HttpResponseRedirect(reverse('activities:index'))
        else:
            return render(request, 'activities/add.html', {'form':form})

    return render(request, "activities/add.html", {'form':AddList()})

