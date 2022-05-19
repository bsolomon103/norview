from django import forms

class SankeyForm(forms.Form):
    file_name = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder':'File Name','style': 'max-width: 300px;', 'class':'form-control'}))
    figure_title = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder':'Figure Title','style': 'max-width: 300px;', 'class':'form-control'}))
    columns = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder':'Column(s)','style': 'max-width: 300px;', 'class':'form-control'}))
    exclude_column = forms.CharField(required=False, widget=forms.TextInput(attrs={'size':25,'placeholder':'Exclude Column', 'style': 'max-width: 300px;','class':'form-control'}))
    exclude_value = forms.CharField(required=False, widget=forms.TextInput(attrs={'size':25,'placeholder':'Exclude Value','style': 'max-width: 300px;', 'class':'form-control'}))
    filter_column = forms.CharField(required=False, widget=forms.TextInput(attrs={'size':25,'placeholder':'Filter Column','style': 'max-width: 300px;', 'class':'form-control'}))
    filter_value = forms.CharField(required=False, widget=forms.TextInput(attrs={'size':25,'placeholder':'Filter Value','style': 'max-width: 300px;', 'class':'form-control'}))
    data = forms.FileField()

class TreeForm(forms.Form):
    file_name = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder':'File Name','style': 'max-width: 300px;', 'class':'form-control'}))
    constant =  forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder':'Constant','style': 'max-width: 300px;', 'class':'form-control'}))
    value = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder':'Aggregate On','style': 'max-width: 300px;', 'class':'form-control'}))
    hover_data = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder':'Hover Data','style': 'max-width: 300px;', 'class':'form-control'}))
    columns = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder':'Column(s)','style': 'max-width: 300px;', 'class':'form-control'}))
    data = forms.FileField()


class TableForm(forms.Form):
    file_name = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder':'File Name','style': 'max-width: 300px;', 'class':'form-control'}))
    columns = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder':'Column(s)','style': 'max-width: 300px;', 'class':'form-control'}))
    data = forms.FileField()
    
class ScatterForm(forms.Form):
    file_name = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder':'File Name','style': 'max-width: 300px;', 'class':'form-control'}))
    x = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder':'X - Axis','style': 'max-width: 300px;', 'class':'form-control'}))
    y = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder':'Y - Axis','style': 'max-width: 300px;', 'class':'form-control'}))
    color = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder':'Color','style': 'max-width: 300px;', 'class':'form-control'}))
    size = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder':'Size','style': 'max-width: 300px;', 'class':'form-control'}))
    data = forms.FileField()
    
class DonutForm(forms.Form):
    file_name = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder':'File Name','style': 'max-width: 300px;', 'class':'form-control'}))
    donuts = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder':'Donuts','style': 'max-width: 300px;', 'class':'form-control'}))
    aggregator = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder':'Aggregator','style': 'max-width: 300px;', 'class':'form-control'}))
    title_text = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder':'Title Text','style': 'max-width: 300px;', 'class':'form-control'}))
    method = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder':'Method','style': 'max-width: 300px;', 'class':'form-control'}))

    data = forms.FileField()


    

    

    

    


    

    
    