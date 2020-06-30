from django.shortcuts import render
from .models import Contact

# Create your views here.
def index(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        msg = request.POST.get('msg', '')
        contact = Contact(name=name, email=email, subject=subject, msg=msg)
        contact.save()
    return render(request,'index.html')
