from django.shortcuts import render
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable1":"this is Swapnali",
        "variable2":"this is Bhandare"
    }
    messages.success(request, "This is a testing message")
    return render(request,'index.html',context)
   # return HttpResponse("This is homepage")

def about(request):
    return render(request,'about.html')
    
def services(request):
    return render(request,'services.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, 'Your details are stored, we will contact you soon....')
    return render(request,'contact.html')
    