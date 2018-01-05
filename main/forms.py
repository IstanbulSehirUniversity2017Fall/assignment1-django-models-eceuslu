# -*- coding: utf-8 -*-

from django import forms
from .models import PeriodInfo,AuthorInfo,BookInfo

class PeriodInfoForm(forms.ModelForm):
    id=forms.CharField(max_length=50,widget=forms.HiddenInput())
    is_actual=forms.ChoiceField(label='Is The Literacy Period On Going',choices=((True,'True'),(False,'False')),widget=forms.RadioSelect())

    class Meta:
        model=PeriodInfo
        fields=['id',
                'is_actual',
        ]

class AuthorInfoForm(forms.ModelForm):
    id=forms.CharField(max_length=50,widget=forms.HiddenInput())
    is_alive=forms.ChoiceField(label='Is Author Alive',choices=((True,'True'),(False,'False')),widget=forms.RadioSelect())

    class Meta:
        model=AuthorInfo
        fields=['id',
                'is_alive',
        ]

class BookInfoForm(forms.ModelForm):
    id=forms.CharField(max_length=50,widget=forms.HiddenInput())
    is_digital=forms.ChoiceField(label='Is Book Digital',choices=((True,'True'),(False,'False')),widget=forms.RadioSelect())

    class Meta:
        model=BookInfo
        fields=['id',
                'is_digital',
        ]