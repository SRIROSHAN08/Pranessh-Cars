from django import forms
from .models import *

class CarDetails_Form(forms.ModelForm):
    class Meta:
        model = CarDetails
        fields = '__all__'
        widgets = {
            'vehicle' : forms.TextInput(attrs={'class' : 'form-control'}),
            'fuel_type' :forms.TextInput(attrs={'class' : ' form-control'}),
            'model' :forms.TextInput(attrs={'class' : 'form-control'}),
            'owner': forms.TextInput(attrs={'class': 'form-control'}),
            'gear' : forms.TextInput(attrs={'class':'form-control'}),
            'seats':forms.TextInput(attrs={'class' : 'form-control'}),
            'color':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'km':forms.NumberInput(attrs={'class':'form-control'}),
            'description':forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','rows': 5,'cols': 50,'placeholder': 'Describe the vehicle, condition, and features...'}),label="Vehicle Description",required=True),
            'insurance':forms.TextInput(attrs={'class':'form-control'}),
            'picture1':forms.FileInput(attrs={'class' : 'form-control'}),
            'picture2':forms.FileInput(attrs={'class' : 'form-control'}),
            'picture3':forms.FileInput(attrs={'class' : 'form-control'}),
            'picture4':forms.FileInput(attrs={'class' : 'form-control'}),
            'picture5':forms.FileInput(attrs={'class' : 'form-control'}),
            'picture6':forms.FileInput(attrs={'class' : 'form-control'}),
            'picture7':forms.FileInput(attrs={'class' : 'form-control'}),
            'picture8':forms.FileInput(attrs={'class' : 'form-control'}),
            'picture9':forms.FileInput(attrs={'class' : 'form-control'}),
            'picture10':forms.FileInput(attrs={'class' : 'form-control'}),
            'picture11':forms.FileInput(attrs={'class' : 'form-control'}),
            'picture12':forms.FileInput(attrs={'class' : 'form-control'}),
            'picture13':forms.FileInput(attrs={'class' : 'form-control'}),
            'picture14':forms.FileInput(attrs={'class' : 'form-control'}),
            'picture15':forms.FileInput(attrs={'class' : 'form-control'}),
        }
        
        
class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields='__all__'
        widgets ={
            'name' :forms.TextInput(attrs={'class':'form-control'}),
            'phn_no' :forms.TextInput(attrs={'class' :'form-control'}),
            'email' :forms.EmailInput(attrs={'class' : 'form-control'}),
            'message':forms.TextInput(attrs={'class' : 'form-control'}),
        }