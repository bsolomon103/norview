from django import forms

class AppendForm(forms.Form):
    data_0 = forms.FileField()
    data_1 = forms.FileField()
    data_2 = forms.FileField(required=False)
    data_3 = forms.FileField(required=False)
    