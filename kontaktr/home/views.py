from django.contrib.auth.models import User
from .models import Contact
from django.shortcuts import render, redirect


def saveinfo(request):
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        telephone = request.POST['telephone']
        add = Contact(FirstName=first_name, LastName=last_name, Email=email, Telephone=telephone)
        add.save()
        Data = Contact.objects.all()
        return render(request, "index.html", {'Data': Data})


def index(request):
    Data = Contact.objects.all()
    return render(request, "index.html", {'Data': Data, 'name': 'Bubuka'})


def formupdate(request, _id):
    if request.method == "POST":
        add = Contact.objects.get(id=_id)
        add.FirstName = request.POST["firstname"]
        add.LastName = request.POST["lastname"]
        add.Email = request.POST["email"]
        add.Telephone = request.POST['telephone']
        add.save()
        return redirect("index")


def edit(request, _id):
    Data = Contact.objects.get(id=_id)
    return render(request, 'edit.html', {'Data': Data})


def delete(request, _id):
    add = Contact.objects.get(id=_id)
    add.delete()
    return redirect('index')


def search(request):
    query = request.GET["query1"]
    Data = Contact.objects.filter(ContactNumber__icontains=query)
    params = {'Data': Data}
    return render(request, 'search.html', params)
