# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.http.response import HttpResponse
from django.template import Context
from django.views.generic import ListView
from price.models import Price, PriceLadoga, PriceNekrasova, PricePupish

# Create your views here.


class PriceView(ListView):
	template_name = 'prices.html'
	context_object_name = 'price_list'
	queryset = Price.objects.all()

	def get_context_data(self, **kwargs):
		context = super(PriceView, self).get_context_data(**kwargs)
		context['priceladoga'] = PriceLadoga.objects.all()
		context['pricenekrasova'] = PriceNekrasova.objects.all()
		context['pricepupish'] = PricePupish.objects.all()
		return context