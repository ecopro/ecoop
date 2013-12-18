from django.http import *
import datetime
from django.shortcuts import *
from ayuda import *
from app1.models import *
from django.views.decorators.http import require_http_methods
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


def prova(request):
    if request.method == 'POST': # If the form has been submitted...
        form1 = ClientForm(request.POST) # A form bound to the POST data
        if form1.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            # ara haurem de redireccionar cap a un altre web via post li pasem el valor de l'usuari.
            #a = request.POST.get("valor")
            _id = request.POST.get("valor")
            return HttpResponseRedirect('/fes_comanda?id='+str(_id))
            #return HttpResponse(y.objects.order_by('client')) # Redirect after POST
    else:
        form1 = ClientForm() # An unbound form

    return render(request, 'prova.html', {
        'form': form1,
    })


@require_http_methods(["POST"])
def fes_comanda(request):
    id = request.GET.get("id")
    #return HttpResponse(id)
    if request.method == 'POST': # If the form has been submitted...
        form = FesComandaForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = FesComandaForm() # An unbound form

    return render(request, 'fes_comanda.html', {
        'form': form,
    })
    pass

def comanda(request):
    value = request.GET.get("id")
    #Logs.objects.filter(date=someDate).order_by('name__last_name')
    #comandes = Comanda.objects.order_by('data_recollida_comanda')
    #context = {"comandes":comandes}
    # Client.objects.filter(ref_client='15').order_by('nom_client')
    #return render(request,'comandes.html',context)
    # Comanda.objects.filter(client=Client.objects.filter(ref_client='15').order_by('nom_client')).order_by('ref_comanda')
    # Comanda.objects.filter(client.ref_client='14').order_by('ref_comanda')
    return HttpResponse(value)

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


def veure_comanda(request):
    if request.method == 'POST': # If the form has been submitted...
        form = VeureComandaForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            
            # Process the data in form.cleaned_data
            # ...
            #return HttpResponseRedirect('/thanks/') # Redirect after POST
            _id = request.POST.get("valor")
            return HttpResponseRedirect('/comanda?id='+str(_id))
    else:
        form = VeureComandaForm() # An unbound form

    return render(request, 'veure_comandes.html', {
        'form': form,
    })
