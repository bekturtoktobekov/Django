from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import FormView
from . import models, forms, parser

class ParserView(FormView):
    template_name = 'parser_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('Данные успешно взяты')
        else:
            return super(ParserView).post(request,*args, **kwargs)

