from django import forms
from django.db import models
from app1.models import *
import datetime 


def divendres_tancat(): #comprova si avui es diendres per saber si encara es pot fer la comanda per la proxima setmana o per d'aui 2 setmanes
	#avui = datetime.datetime(2013, 12, 21) #nomes per simular que avui es dv
	avui=datetime.date.today() #agafa el dia actual 
	if avui.weekday()>4:
		return True
	else:
		return False

def dates_entrega():
	divendres=divendres_tancat()
	avui = datetime.date.today()
	if divendres== True :
		avui = avui + datetime.timedelta(days=-avui.weekday() + 1, weeks=2) #si avui es passat dv la comanda sera per d'aqui 2 setmanes
	else:
		avui = avui + datetime.timedelta(days=-avui.weekday() + 1, weeks=1) # si avui encara no es dv la comanda es pot fer per la proxima setmana
	dates_entrega = []
	dates_entrega.append(('1', str(avui)))
	dates_entrega.append(('2', str(avui+datetime.timedelta(weeks=1))))
	dates_entrega.append(('3', str(avui+datetime.timedelta(weeks=2))))
	dates_entrega.append(('4', str(avui+datetime.timedelta(weeks=3))))
	dates_entrega=tuple(dates_entrega)
	return dates_entrega



class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class ClientForm(forms.Form):
	valor_clients=[]
	x=Client.objects.order_by('ref_client')
	for c in x:
		valor_clients.append((c.ref_client , c.nom_client))

	valor_clients=tuple(valor_clients)
	valor = forms.ChoiceField(choices=valor_clients)

class FesComandaForm(forms.Form):
	prod=[]
	x=Producte.objects.order_by('ref_prod')
	for c in x:
		prod.append((c.ref_prod , c.nom_prod))
	prod=tuple(prod)
	productes = forms.ChoiceField(choices=prod)
	quantitat=forms.IntegerField(max_value=12)
	data_entrega = forms.ChoiceField(choices=dates_entrega())
	#valor = forms.ChoiceField(choices=valor_comandes)
