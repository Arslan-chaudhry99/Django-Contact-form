from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.

def contact(request):
  if request.method == "POST":
    firstName=request.POST.get('firstName')
    lastName=request.POST.get('lastName')
    email=request.POST.get('email')
    address=request.POST.get('address')
    zipcode=request.POST.get('zip')
    phone=request.POST.get('phone')
    contact=Contact(firstName=firstName, lastName=lastName, email=email, address=address, zipcode=zipcode, phone=phone, date=datetime.today())
    contact.save()
    
    messages.success(request, 'Dear'+ ' ' + firstName+ ' ' + lastName + ' ' + 'your form has been submited!')
    return redirect('/')
  return render(request,'contact.html')
  