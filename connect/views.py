# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import ConnectForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from article.models import Article

# from django.template.context_processors import csrf

# Create your views here.


def connect(request):	
	form = ConnectForm(request.POST)
	if request.method == 'POST' and form.is_valid():
		form.cleaned_data
		new_form = form.save()
		return HttpResponseRedirect('/thank-you/')
	else:
		return render(request, 'connect.html', locals())


# def thanks(request):
# 	return render_to_response('thanks.html')

def thanks(request, page_number=1):
	all_articles = Article.objects.all()
	current_page = Paginator(all_articles, 2)
	return render_to_response('thanks.html', {'thanks': current_page.page(page_number)})