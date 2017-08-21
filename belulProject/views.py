# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from article.models import Article

# Create your views here.


def mainView(request, page_number=1):
	all_articles = Article.objects.all()
	current_page = Paginator(all_articles, 2)
	return render_to_response('mainpage.html', {'mainView': current_page.page(page_number)})
