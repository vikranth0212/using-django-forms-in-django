from django import forms

from app.models import *

class Topic_form(forms.Form):
    
    #here forms is module,Form is a class

    topic_name=forms.CharField()


class Webpage_form(forms.Form):

    tl=[[to.topic_name,to.topic_name] for to in Topic.objects.all()]
    #in tl[0][0] primarykey column value is there that 1 need to carry BE
    # in tl[0][1]  need to display in FE
    topic_name=forms.ChoiceField(choices=tl)
    name=forms.CharField()
    url=forms.URLField()
    email=forms.EmailField()
    

class Accessrecord_form(forms.Form):
    wl=[[wo.pk,wo.name] for wo in Webpage.objects.all()]
    # in wl[0][0] wo.pk is primary key column in wepage model or table and forwarded to BE
    # in wl[0][1] wo.name is a name column in webpage and it will display in FE in html page form
    name=forms.ChoiceField(choices=wl)
    author=forms.CharField()
    date=forms.DateField()

