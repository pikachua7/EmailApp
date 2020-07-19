from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    if request.method=='POST':
        message = request.POST['message']
        send_mail('ENTER YOUR SUBJECT HERE',
                  message,
                  settings.EMAIL_HOST_USER,
                  ['ENTER RECEIVER EMAIL HERE'],
                  fail_silently=False)
    return render(request,'emailapp/email.html')

