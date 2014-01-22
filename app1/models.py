from django.db import models
from django.contrib.auth.models import User # fem un import de la llibreria de usuaris de sistema de django, aixis que quan creem un usuari de sistema passa a ser automaticament un client
from django.db.models.signals import post_save # despres de crear el usuari de sistema quens crei el client tambe

# Create your models here.

class Model1(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    choice_text = models.CharField(max_length=4)
    votes = models.IntegerField(default=0)

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class Comissio(models.Model):
    nom = models.CharField(max_length=254)
    def __unicode__(self):
        return "comissio %s"%self.nom

class Client(models.Model):
    TORNS = ( ("ex","Exempt"), ("ca","Caixes"), ("re","Recollida") )
    user = models.OneToOneField(User)
    # ref_client -> num_caixa
    num_caixa = models.IntegerField(default=0)
    nom_client = models.CharField(max_length=254)
    torn = models.CharField( max_length=2, choices=TORNS, default="ca" )
    max_torns = models.PositiveIntegerField(default=4)
    comissio = models.ForeignKey(Comissio,null=True)
    def __str__(self):
          return "Caixa[%s]: %s" % (self.num_caixa,self.user)

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = Client.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User)  


class Event(models.Model):
    data = models.DateTimeField()
    desc = models.CharField(max_length=1024,default="Recollida de comandes")
    caixa_1 = models.ForeignKey(Client,null=True,blank=True,related_name="caixa1")
    caixa_2 = models.ForeignKey(Client,null=True,blank=True,related_name="caixa2")
    caixa_3 = models.ForeignKey(Client,null=True,blank=True,related_name="caixa3")
    caixa_4 = models.ForeignKey(Client,null=True,blank=True,related_name="caixa4")
    caixa_5 = models.ForeignKey(Client,null=True,blank=True,related_name="caixa5")
    recollida_1 = models.ForeignKey(Client,null=True,blank=True,related_name="reco1")
    recollida_2 = models.ForeignKey(Client,null=True,blank=True,related_name="reco2")
    recollida_3 = models.ForeignKey(Client,null=True,blank=True,related_name="reco3")
    recollida_4 = models.ForeignKey(Client,null=True,blank=True,related_name="reco4")
    recollida_5 = models.ForeignKey(Client,null=True,blank=True,related_name="reco5")
    
    def __unicode__(self):
        return unicode(self.data)+"    "+unicode(self.desc)
    def caixa(self):
        torns = []
        if self.caixa_1:
            torns.append(self.caixa_1)
        if self.caixa_2:
            torns.append(self.caixa_2)
        if self.caixa_3:
            torns.append(self.caixa_3)
        if self.caixa_4:
            torns.append(self.caixa_4)
        if self.caixa_5:
            torns.append(self.caixa_5)
        return torns

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

