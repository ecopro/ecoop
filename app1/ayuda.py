from django import forms
from django.db import models
from app1.models import *
import datetime 
import random





class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class ClientForm(forms.Form):
	valor = forms.ChoiceField()
	
	def __init__(self, *args, **kwargs):
		super(ClientForm, self).__init__(*args, **kwargs)
		self.fields['valor']=forms.ChoiceField(choices=torna_clients())

class FesComandaForm(forms.Form):
	productes = forms.ChoiceField()
	quantitat=forms.IntegerField(max_value=12)
	data_entrega = forms.ChoiceField()
	client_id = forms.IntegerField()
	
	def __init__(self, *args, **kwargs):
		super(FesComandaForm, self).__init__(*args, **kwargs)
		self.fields['productes']=forms.ChoiceField(choices=torna_productes())
		self.fields['data_entrega']=forms.ChoiceField(choices=dates_entrega())

class VeureComandaForm(forms.Form):
	valor = forms.ChoiceField()

	def __init__(self, *args, **kwargs):
		super(VeureComandaForm, self).__init__(*args, **kwargs)
		self.fields['valor']=forms.ChoiceField(choices=torna_clients())





# ----- Funcions per aleugerir les classes -----

# Funcio que torna la llista actual de tots els productes
def torna_productes():
	prod=[]
	x=Producte.objects.order_by('ref_prod')
	for c in x:
		prod.append((c.ref_prod , c.nom_prod))
	prod=tuple(prod)
	return prod


# Funcio que torna la llista actual de tots els clients
def torna_clients():
	valor_clients=[]
	x=Client.objects.order_by('ref_client')
	for c in x:
		valor_clients.append((c.ref_client , c.nom_client))
	valor_clients=tuple(valor_clients)
	return valor_clients


# Funcio que genera les 4 proximes dates d'entrega per l'usuari tenint en compte el dia actual
def dates_entrega():
	divendres=divendres_tancat()
	avui = datetime.date.today()
	if divendres== True :
		avui = avui + datetime.timedelta(days=-avui.weekday() + 1, weeks=2) #si avui es passat dv la comanda sera per d'aqui 2 setmanes
	else:
		avui = avui + datetime.timedelta(days=-avui.weekday() + 1, weeks=1) # si avui encara no es dv la comanda es pot fer per la proxima setmana
	dates_entrega = []
	dates_entrega.append((str(avui), str(avui)))
	dates_entrega.append((str(avui+datetime.timedelta(weeks=1)), str(avui+datetime.timedelta(weeks=1))))
	dates_entrega.append((str(avui+datetime.timedelta(weeks=2)), str(avui+datetime.timedelta(weeks=2))))
	dates_entrega.append((str(avui+datetime.timedelta(weeks=3)), str(avui+datetime.timedelta(weeks=3))))
	dates_entrega=tuple(dates_entrega)
	return dates_entrega


# Funcio que torna si avui es dv per saber si encara es pot realitzar la comanda per el proxim dimarts  (relacionat amb funct dates_entrega)
def divendres_tancat(): #comprova si avui es diendres per saber si encara es pot fer la comanda per la proxima setmana o per d'aui 2 setmanes
	#avui = datetime.datetime(2013, 12, 21) #nomes per simular que avui es dv
	avui=datetime.date.today() #agafa el dia actual 
	if avui.weekday()>4:
		return True
	else:
		return False

def torna_client_by_id(id):
	client=Client.objects.filter(ref_client='15')
	return client

def torna_comandes_by_client(id_client):
	llista_comandes=[]
	client = torna_client_by_id(id_client)
	comandes = Comanda.objects.filter(client=client)
	for comanda in comandes:
		llista_comandes.append((comanda.ref_comanda, comanda.data_recollida_comanda))
	llista_comandes=tuple(llista_comandes)

	return llista_comandes


#dic={client_id : client_id, producte: producte, quantitat:quantitat, data_entrega:data_entrega}
def grabar_comanda(dic):
	#client = dic[client]
	#prod = dic[producte]
	#quantitat = dic[quantitat]
	#data_entrega = dic[data_entrega]
	ref_com=random.randint(0,299)
	client_inst= Client.objects.filter(ref_client=dic['client'])
	new_comanda = Comanda(ref_comanda=ref_com, client=client_inst)
	new_comanda.save()

	new_detall_comanda= DetallComanda(producte=dic[producte], quantitat_demanada=dic[quantitat], comanda=new_comanda)
	new_detall_comanda.save()

	