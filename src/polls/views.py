from django.http import HttpResponseRedirect, Http404, HttpResponse
from polls.models import Choice, Poll
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.core import serializers


class AJAXListMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if not request.is_ajax():
            raise Http404("This is an ajax view, friend.")

        return super(AJAXListMixin, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super(AJAXListMixin, self).get_queryset()

    def get(self, request, *args, **kwargs):
        return HttpResponse(serializers.serialize('json', self.get_queryset()))


class IndexView(AJAXListMixin, generic.ListView):
    template_name = "polls/main.html"
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """
        Return the last five published polls (not including those set to be
        published in the future).
        """
        return Poll.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Poll
    template_name = "polls/detail.html"

    def get_queryset(self):
        return Poll.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Poll
    template_name = "polls/result.html"

    def get_queryset(self):
        return Poll.objects.filter(pub_date__lte=timezone.now())


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))