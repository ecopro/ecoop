from django import forms
from django.db import models
from app1.models import *


valor_clients=[]
x=Client.objects.order_by('ref_client')

for c in x:
	valor_clients.append((c.ref_client , c.nom_client))

valor_clients=tuple(valor_clients)

'''valor_comandes=[]
y=Comanda.objects.get(ref_comanda='1030')

for d in y:
	valor_comandes.append((d , d))

valor_comandes=tuple(valor_comandes)
'''

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class ClientForm(forms.Form):
    valor = forms.ChoiceField(choices=valor_clients)

class RealitzaComanda(forms.Form):
	b = Comanda.objects.order_by('client')
	#valor = forms.ChoiceField(choices=valor_comandes)
