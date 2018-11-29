from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ColumnsAmountForm


# Create your views here.
class Columns(FormView):
    template_name = 'app_main/main.html'
    form_class = ColumnsAmountForm
    success_url = '/'

    def form_valid(self, form):
        return super(Columns, self).form_valid(form)

