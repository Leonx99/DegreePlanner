from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Class
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'planner/index.html'
    context_object_name = 'classes'

    def get_queryset(self):
        return Class.objects.all()

class EligibleView(generic.ListView):
    template_name = 'planner/eligible.html'
    context_object_name = 'eligible_classes'

    def get_queryset(self):
        elig_class = Class.objects.filter(elig=False) # gets all clases that aren't eligible
        elig_class = elig_class.filter(taken=False) # filters all courses that aren't eligeble and haven't been taken yet
        for stuff in elig_class: # iterator
            req1 = stuff.pre_req1 # gets the data in pre_req1 field
            #req2 = stuff.pre_req2
            #req3 = stuff.pre_req3
            c1 = Class.objects.get(name = req1) # gets the class(object) with the name and checks if that class (the prerequisite) has been taken
            #c2 = Class.objects.get(name = req2)
            #c3 = Class.objects.get(name = req3)
            if c1.taken == True: #if the pre_req has been taken the class is updated to eligible.
                stuff.elig = True
                stuff.save() # saves the update
        return Class.objects.filter(elig=True)

class TakenView(generic.ListView):
    template_name = 'planner/taken.html'
    context_object_name = 'taken_classes'

    def get_queryset(self):
        return  Class.objects.filter(taken=True)
    
