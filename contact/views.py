# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView

from django.http import HttpResponseRedirect

from .models import Contact
from .forms import ContactForm

# Create your views here.
class HomePageView(TemplateView):
	def get(self,request, **kwargs):
		return render(request, 'index.html', context=None)

class AddPageView(TemplateView):
	def get(self,request, **kwargs):

		return render(request, 'contact_form.html', context={'form': ContactForm()})

	def post(self,request):
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add')
		return render(request, 'contact_form.html', context={'form': form})

class ListPageView(TemplateView):
	def get(self,request, **kwargs):
		all_contacts = Contact.objects.all()
		return render(request, 'list.html', {'all_contacts': all_contacts})

class AboutPageView(TemplateView):
	def get(self,request, **kwargs):
		template_name = "about.html"
		return render(request, template_name, context=None)
