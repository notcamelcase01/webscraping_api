from django import forms

class NameForm(forms.Form):
    page_no = forms.IntegerField(label="Enter Page Number")