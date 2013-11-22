from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from polls.models import Poll, Choice
from django.template import RequestContext, loader

# Create your views here.

def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	#template = loader.get_template('polls/index.jade')
	#context = RequestContext(request, {
	#	'latest_poll_list': latest_poll_list,
	#})
	#return HttpResponse(template.render(context))
	return render(request, 'polls/index.jade', {'latest_poll_list': latest_poll_list})

def detail(request, poll_id):
	#try:
	#	poll = Poll.objects.get(pk=poll_id)
	#	choice = Choice.objects.filter(poll=poll_id)
	#except Poll.DoesNotExist:
	#	raise Http404
	#el siguiente codigo es un atajo para resumir el codigo anterior comentado
	poll = get_object_or_404(Poll, pk=poll_id)
	choice = Choice.objects.filter(poll=poll_id)
	#atajo de codigo de rendereado para que quede en una sola linea
	return render(request, 'polls/detail.jade', {'poll': poll, 'choice': choice})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
    	selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
    	return render(request, 'polls/detail.jade', {
    		'poll': p,
    		'error_message': "you didn't select a choice.",
    		})
    else:
    	selected_choice.votes += 1
    	selected_choice.save()
    	return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))