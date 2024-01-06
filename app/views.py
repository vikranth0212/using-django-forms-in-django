from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from app.forms import *
# Create your views here.

def insert_topic(request):

    ETFO=Topic_form()
    d={'EFOTOPIC':ETFO}
    #ETFO empty topic form object
    #in forms module we created a topicform that 1 we are calling here,
    #ETFO is a empty object with ETFO we are calling topicform()
    if request.method=='POST':

        #after submitting  data in html page request.method will get activated 
        TFDO=Topic_form(request.POST)
        #TFDO means topic form data object
        #request.POST ia a dict related to html foms,it will create django itself
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            #cleaned_data is a dict related to django forms,after submit data it will store here
            # in Topic Object inserted data will get or create and it will display in tuple,
            #so we are using [0] at end of TO
            TO.save()

            return HttpResponse('data inserted successfully')
            # it will give response
            # if we give render of html page we need to add 1 html page
        else:
            return render('invalid data')    

    return render(request,'insert_topic.html',d)    

def insert_webpage(request):
    EWFO=Webpage_form()
    d={'EWF':EWFO}
    if request.method=='POST':

        WFDO=Webpage_form(request.POST)

        if WFDO.is_valid():

            tn=WFDO.cleaned_data['topic_name']

            TO=Topic.objects.get(topic_name=tn)

            n=WFDO.cleaned_data['name']
            u=WFDO.cleaned_data['url']
            e=WFDO.cleaned_data['email']
            
            WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
            WO.save()
            
            return HttpResponse('data inserted in webpage')

    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    EAFO=Accessrecord_form()
    d={'EAF':EAFO}
    if request.method=='POST':
        AFDO=Accessrecord_form(request.POST)
        if AFDO.is_valid():
            nm=AFDO.cleaned_data['name']
            WO=Webpage.objects.get(pk=nm)
            ath=AFDO.cleaned_data['author']
            dt=AFDO.cleaned_data['date']

            AO=Accessrecord.objects.get_or_create(name=WO,author=ath,date=dt)[0]
            AO.save()
            return HttpResponse('accessrecord created') 
        else:
            return HttpResponse('invalid') 
    return render(request,'insert_accessrecord.html',d)              








