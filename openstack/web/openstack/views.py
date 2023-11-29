from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
from django.contrib import messages
from openstack.models import instance
from openstack.forms import instanceForm
from openstack.forms import instanceFormMahasiswa

# Create your views here.
# Dashboard

def dashboard(request):
    data_dashboard = instance.objects.all()
    return render(request, 'dashboard.html', {'data_dashboard': data_dashboard})

def add_instance(request):
    if request.user.is_staff:
        form = instanceForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    else:
        form = instanceFormMahasiswa(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    return render(request, 'add_form.html', {'form': form})

def edit_instance(request, pk):
    edit_instance = get_object_or_404(instance, pk=pk)
    form = instanceForm(request.POST or None, instance=edit_instance)
    if form.is_valid():
        form.save()
        return redirect('/dashboard')
    return render(request, 'add_form.html', {'form': form})

