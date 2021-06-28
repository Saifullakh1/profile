from django.shortcuts import render, redirect
from .models import Profile


def index(request):
    profile = Profile.objects.all()
    return render(request, 'index.html', {'profile': profile})


def create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birth_date = request.POST.get('birth_date')
        is_worker = request.POST.get('is_worker')
        pr_obj = Profile.objects.create(first_name=first_name, last_name=last_name, birth_date=birth_date, is_worker=is_worker)
        pr_obj.save()
        return redirect('index')
    return render(request, 'profes/create.html')


def detail(request, id):
    prof = Profile.objects.get(id=id)
    return render(request, 'detail.html', {'prof': prof})


def update(request, id):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birth_date = request.POST.get('birth_date')
        is_worker = request.POST.get('is_worker')
        prof = Profile.objects.get(id=id)
        prof.firs_name = first_name
        prof.last_name = last_name
        prof.birth_date = birth_date
        prof.is_worker = is_worker
        prof.update()
        return redirect(index)
    return render(request, 'update.html')


def delete(request, id):
    if request.method == 'POST':
        prof = Profile.objects.get(id=id)
        prof.delete()
        return redirect('index')
    return render(request, 'posts/delete.html')







