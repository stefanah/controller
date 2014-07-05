from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    #template = loader.get_template('login/index.html')
    template = loader.get_template('Goal_Light_Site/index.html')
    #context = RequestContext(request, {'content':'content'})
    context = RequestContext(request)
    return HttpResponse(template.render(context))

#def index(request):
#    #template = loader.get_template('login/index.html')
#    return HttpResponse('hello world')