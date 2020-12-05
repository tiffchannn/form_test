from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,"index.html")

def create_user(request):
    print("*"*60)
    print("Got Post Info.........")
    print("Name: ", request.POST['name'])
    print("Email: ", request.POST['email'])
    print("Number: ", request.POST['phone'])
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    phone_number = request.POST['phone']
    context = {
        "name_on_template": name_from_form,
        "email_on_template": email_from_form,
        "phone_number": phone_number
    }
    return render(request, "show.html", context)

def success(request):
    return render(request, "show.html")
