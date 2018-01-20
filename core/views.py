from django.shortcuts import render
from core.models import StudioItems
from core.forms import MessagesForm
from django.contrib import messages
from django.core.mail import send_mail



# Create your views here.
def error_404(request):
    return render(request, '404.html')

def error_500(request):
    return render(request, '500.html')

def offeringView(request):
    form = MessagesForm()
    if request.method == 'POST':
        form = MessagesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Thank you for reaching out to me. I will get back to you soon')
            return render(request,'offering.html',{'form':form})
    return render(request,'offering.html',{'form':form})

def studioView(request):
    items = StudioItems.objects.all();
    form = MessagesForm()
    if request.method == 'POST':
        form = MessagesForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
            message = form.cleaned_data['message']
            email_message = [name,email,contact,message]
            form.save()
            send_mail('Inbound', str(email_message), 'tawahid@gmail.com', ['tawahid@gmail.com'], fail_silently=True)
            send_mail('Thaha Abdul Wahid - Message','Thank you for reaching out to me. I have recieved your email. Will get back to you with a reply soon.','project.wsms@gmail.com',[str(email)], fail_silently=True)
            messages.success(request, 'Thank you for reaching out to me. I will get back to you soon')
            return render(request, 'offering.html', {'form': form, 'items':items})
    return render(request,'studio.html',{'form':form,'items':items})