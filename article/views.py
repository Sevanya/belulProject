# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.http.response import HttpResponse
from django.template import Context
from django.core.paginator import Paginator
from article.models import Article

# Create your views here.


def articles(request, page_number=1):
	all_articles = Article.objects.all()
	current_page = Paginator(all_articles, 3)
	return render_to_response('articles.html', {'articles': current_page.page(page_number)})

def article(request, article_id=1):
	return render_to_response('article.html', {'article': Article.objects.get(id=article_id)})
