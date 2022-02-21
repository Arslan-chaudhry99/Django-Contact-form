from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
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
  return render(request, 'contact.html')
  # return HttpResponse('i am contact')