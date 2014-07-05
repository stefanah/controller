from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from forms import GoalLightForm
from models import GoalLight
import json

import logging
log = logging.getLogger(__name__)

@login_required
def index(request):
    #template = loader.get_template('login/index.html')
    #template = loader.get_template('controlProjects/index.html')
    #context = RequestContext(request, {'content':'content'}) #(hello)
    #return HttpResponse(template.render(context))
    return render( request, 'controlProjects/index.html')

@login_required
def goalLight(request):
    #context = RequestContext(request)
    user = request.user

    goal = GoalLight.objects.get(user = user)
    print goal, goal
    if request.method == 'POST':
        form = GoalLightForm(user, goal, request.POST, instance=goal)
        
        if form.is_valid():
            form.save(commit=True)
            
        else:
            print form.errors
    else:
        form = GoalLightForm(user, goal)
    return render( request, 'controlProjects/GoalLight.html', {'form': form} )   #'str' object has no attribute 'META'
    #return render( request, 'controlProjects/goalLight.html' )

@login_required
def goalLightRaw(request):
    instance = GoalLight.objects.get(user=request.user)
    goalData = {'onTime':instance.onTime,
                'soundOn':instance.soundOn,
                'lightOn':instance.lightOn}
    goalData = json.dumps(goalData)

    log.debug("Hey there it works!!")
    log.info("Hey there it works!!")
    log.warn("Hey there it works!!")
    log.error("Hey there it works!!")

    instance.onTime = 0
    instance.save(update_fields=['onTime'])
    return HttpResponse(goalData)
#    return HttpResponse('Raw text in dict format for RPi to read')

def anotherProject(request):
    return HttpResponse('another project page that should only be seen by me')
