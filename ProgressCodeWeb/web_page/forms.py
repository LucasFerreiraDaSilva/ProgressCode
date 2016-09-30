from django import forms
from django.contrib import admin
from web_service.models import *

class EventoForm(forms.ModelForm):
	class Meta:
		model = Evento
		fields = ('nome_evento', 'descricao')

class TutorForm(forms.ModelForm):
	class Meta:
		model = Tutor
		fields = ('nome', 'email', 'senha')

class EncontroForm(forms.ModelForm):
	class Meta:
		model = Encontro
		fields = ('data_realizao', 'evento')