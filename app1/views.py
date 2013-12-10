from django.http import *
import datetime
from django.shortcuts import *
from ayuda import *
from app1.models import *
# Create your views here.
#return render_to_response('sometemplate.html')

def basic(request):
    return HttpResponse("Hello world")


def data_hora(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def clients(request):
    clients = Client.objects.order_by('nom_client')
    context = {"clients":clients}
    return render(request,'clients.html',context)

def thanks(request):
    return render_to_response('thanks.html')


def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, 'contact.html', {
        'form': form,
    })

def veureproductesclient(request):
    #if 'clients' in request.POST:
    selected_packages =request.POST.get("resposta") 
    #else:
        #selected_packages = 'You submitted an empty form.'
    #return HttpResponse(message)
    return HttpResponse(selected_packages)


def comanda(request):
    comandes = Comanda.objects.order_by('data_recollida_comanda')
    context = {"comandes":comandes}
    return render(request,'comandes.html',context)

def producte(request):
    productes = Producte.objects.order_by('nom_prod')
    context = {"productes":productes}
    return render(request,'producte.html',context)

def detall_comanda(request):
    detalls = DetallComanda.objects.order_by('quantitat_demnada')
    context = {"detalls":detalls}
    return render(request,'detall_comanda.html',context)


def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)