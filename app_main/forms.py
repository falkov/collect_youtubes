from django import forms

class ColumnsAmountForm(forms.Form):
    columns = forms.IntegerField(min_value=1, max_value=10)
