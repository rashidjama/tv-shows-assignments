from django.shortcuts import render, redirect
from .models import Show

# Create your views here.
def index(request):
  context = {
    "shows": Show.objects.all()
  }
  return render(request, "shows.html", context)

def new(request):
  return render(request, "new.html")

def create(request):
  Show.objects.create(
    title = request.POST['title'],
    newwork= request.POST['network'],
    released = request.POST['r_date'],
    description = request.POST['des']
  )
  return redirect('/')

def show(request, show_id):
  single_show = Show.objects.get(id=show_id)
  context = {
    'show': single_show
  }
  return render(request, "show.html", context)

def edit(request, show_id):
  edit_show = Show.objects.get(id=show_id)
  context = {
    'show': edit_show
  }
  return render(request, "edit.html", context)

def update(request, show_id):
  to_update = Show.objects.get(id=show_id)
  to_update.title = request.POST['title']
  to_update.newwork = request.POST['network']
  to_update.released = request.POST['r_date']
  to_update.description = request.POST['des']

  to_update.save()

  return redirect("/")

def delete(request, show_id):
  to_del = Show.objects.get(id=show_id)
  to_del.delete()
  return redirect('/')