from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable' : 'this is sent 💯',
        'variable1' : 'invalid transaction 👎',
        'variable2' : 'this is not valid 🥇'
    }
#    messages.success(request, "This is a test message")
    return render(request, 'index.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        desc = request.POST.get('desc')
        # Contact object create object name = element
        element = Contact(name=name, email=email, number=number, desc=desc, date=datetime.today())
        element.save()
        messages.success(request, "Your message has been sent!!")

    return render(request, 'contact.html')
    #return HttpResponse("<h1>Hello, Fill Your contact Details...</h1>")

def about(request):
    return HttpResponse("<h1>Hello, This is About...</h1>")

def cart(request):
    return HttpResponse("<h1>Cart : Pay Your Bill..</h1>")