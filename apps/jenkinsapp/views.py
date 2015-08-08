from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .forms import MemberForm
from .models import Member
# Create your views here.


def home(request):
    data = {'subtitle': 'Home'}
    template = 'jenkinsapp/index.html'
    return render_to_response(template, data, context_instance=RequestContext(request))

def list(request):
    members = Member.objects.all()
    data = {'subtitle': 'List Member', 'members': members}
    template = 'jenkinsapp/list.html'
    return render_to_response(template, data, context_instance=RequestContext(request))

def add(request):
    form = MemberForm(request.POST or None)
    if form.is_valid():
        urls = form.save()
        messages.success(request, "Add Member Success.")
        return HttpResponseRedirect(reverse('list'))

    data = {'subtitle': 'Add Member', 'form': form}
    template = 'jenkinsapp/add.html'
    return render_to_response(template, data, context_instance=RequestContext(request))
