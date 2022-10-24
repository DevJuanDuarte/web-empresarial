from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
# Create your views here.

def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')


            #CREAMOS EL CORREO 
            email = EmailMessage(
                "La sabrosa: Nuevo mensaje de contacto",#asunto
                "De {} {}\n\nEscribió:\n\n{}".format(name,email,content), #mensaje
                "lasabrosa.com", #Email de origen
                ["juan.devcontact@gmail.com"],#email destino
                reply_to=[email]
            )

            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")


    return render(request, 'contact/contact.html', {'form':contact_form})