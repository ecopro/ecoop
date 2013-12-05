from django.db import models
from django.contrib.auth.models import User # fem un import de la llibreria de usuaris de sistema de django, aixis que quan creem un usuari de sistema passa a ser automaticament un client
from django.db.models.signals import post_save # despres de crear el usuari de sistema quens crei el client tambe

# Create your models here.

class Model1(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    choice_text = models.CharField(max_length=4)
    votes = models.IntegerField(default=0)

class Client(models.Model):
	user = models.OneToOneField(User)
	ref_client = models.IntegerField(default=0)
	nom_client = models.CharField(max_length=254)
	def __str__(self):  
          return "client %s" % self.user

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = Client.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User)  

class Proveidor(models.Model):
	ref_prov = models.IntegerField(default=0)
	nom_prov = models.CharField(max_length=50)
	nif_prov = models.CharField(max_length=15)
	email_prov = models.EmailField(max_length=254)

	def __unicode__(self):
		return  self.nom_prov

class Producte(models.Model):
	ref_prod = models.IntegerField(default=0)
	nom_prod = models.CharField(max_length=50)
	quantitat_prod = models.IntegerField(default=0)  
	preu_prod  = models.FloatField()
	tipus_prod  =models.BooleanField() # si el producte es fresc o de stock
	proveidor_prod = models.ForeignKey(Proveidor)
	um_prod = models.BooleanField() #um_prod voll dir unitat de mesura del producte
	def __unicode__(self):
		return  self.nom_prod

class Comanda(models.Model):
	ref_comanda = models.IntegerField(default=0)
	data_creacio_comanda = models.DateTimeField('data creacio')
	data_recollida_comanda = models.DateTimeField('data recollida')
	data_entreaga_comanda = models.DateTimeField('data entrega')
	client = models.ForeignKey(Client)
	def __unicode__(self):
		return "%s " % self.ref_comanda

class DetallComanda(models.Model):
	producte = models.ForeignKey(Producte)
	quantitat_demnada = models.FloatField()
	quantitat_entregada = models.FloatField()
	comanda = models.ForeignKey(Comanda)
	def __unicode__(self):
		return "Comanda nr: %s " % self.comanda



		

