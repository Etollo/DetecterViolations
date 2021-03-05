from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View

from DetecterViolation import constants
from violation.forms import ViolationForm
from violation.models import Violation
from violation.utils import ObjectDeleteMixin, ObjectUpdateMixin, ObjectViolationMixin
from rest_framework import generics
from violation.serializers import ViolationDetailSerializer


class ViolationCreateView(generics.CreateAPIView):
    serializer_class = ViolationDetailSerializer


class ViolationSave(View):
    nbar = constants.NBAR_VIOLATION_SAVE
    model_form = ViolationForm
    template = "violation/violation_save.html"

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, context={'form': form, 'nbar': self.nbar})

    def post(self, request):
        bound_form = self.model_form(data=request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})


class ViolationDetail(ObjectViolationMixin, View):
    model = Violation
    template = 'violation/violation_detail.html'
    nbar = constants.NBAR_VIOLATION


class ViolationUpdate(ObjectUpdateMixin, View):
    model = Violation
    model_form = ViolationForm
    template = 'violation/violation_update.html'
    nbar = constants.NBAR_VIOLATION


class ViolationDelete(ObjectDeleteMixin, View):
    model = Violation
    template = 'violation/violation_delete.html'
    redirect_url = 'violation_list_url'
    nbar = constants.NBAR_VIOLATION


class ViolationList(View):
    nbar = constants.NBAR_VIOLATION

    def get(self, request):
        violations = Violation.objects.all()

        return render(request, 'violation/violation_list.html', context={'violation': violations, 'nbar': self.nbar})


@login_required
def violation_json(request):
    violations = Violation.objects.all()
    json = serializers.serialize('json', violations)
    return HttpResponse(json, content_type='application/json')