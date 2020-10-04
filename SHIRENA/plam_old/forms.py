# -*- coding: utf-8 -*-
from django import forms
from .models import Message, Pallets , Company,CompanyRelated


class MessageForm(forms.ModelForm):
    rcvCompanycode=forms.CharField(max_length = 5, required = True)
    message = forms.CharField(widget=forms.Textarea(), max_length=300)

    class Meta:
        model = Message
        fields = ['rcvCompanycode', 'message']


class pl_adjust(forms.Form):
    keyid = forms.CharField(max_length=10)
    PLtype = forms.CharField(max_length=1)
    PLvolume =forms.CharField(max_length=5)
    sndCompanycode=forms.CharField(max_length=5)
    rcvCompanycode=forms.CharField(max_length=5)
    sndDate = forms.DateField()
    rcvDate = forms.DateField()    



class nyukoForm(forms.ModelForm):
    keyid = forms.CharField(max_length=10)
    PLtype = forms.CharField(max_length=1)
    PLname = forms.CharField(max_length=100)
    PLvolume =forms.CharField(max_length=5)
    sndCompanycode=forms.CharField(max_length=5)
    rcvCompanycode=forms.CharField(max_length=5)
    sndDate = forms.DateField()
    rcvDate = forms.DateField()
    
    class Meta:
        model = Pallets
        fields = ['keyid', 'PLtype','PLname','PLvolume','sndCompanycode','rcvCompanycode','sndDate','rcvDate']
                

class CompanyForm(forms.ModelForm):
    companyCode = forms.CharField(max_length = 5, required = True)
    companyName = forms.CharField(max_length = 100, required = True)

    class Meta:
        model = Company
        fields = ['companyCode', 'companyName']
        
class CompanyRelatedForm(forms.ModelForm):
    keycompanyCode = forms.CharField(max_length = 5, required = True)
    keycompanyName = forms.CharField(max_length = 100, required = True)
    relatedcompanyCode = forms.CharField(max_length = 5, required = True)
    relatedcompanyName = forms.CharField(max_length = 100, required = True)
    
    class Meta:
        model = CompanyRelated
        fields = ['keycompanyCode', 'keycompanyName','relatedcompanyCode','relatedcompanyName']
    