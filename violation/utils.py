from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse


class ObjectViolationMixin:
    model = None
    template = None
    nbar = None

    def get(self, request, id):
        obj = get_object_or_404(self.model, id=id)
        return render(request, self.template, context={self.model.__name__.lower(): obj, 'nbar': self.nbar})


class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None
    nbar = None

    def get(self, request, id):
        obj = self.model.objects.get(id=id)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template,
                      context={'form': bound_form, self.model.__name__.lower(): obj, 'nbar': self.nbar})

    def post(self, request, id):
        obj = self.model.objects.get(id=id)
        bound_form = self.model_form(data=request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()

            if new_obj.is_active == 1:
                qs = self.model.objects.exclude(id=new_obj.id)
                print(qs)
                qs.update(is_active=0)

            return redirect(new_obj)

        return render(request, self.template,
                      context={'form': bound_form, self.model.__name__.lower(): obj, 'nbar': self.nbar})


class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None
    nbar = None

    def get(self, request, id):
        obj = self.model.objects.get(id=id)
        return render(request, self.template,
                      context={self.model.__name__.lower(): obj, 'nbar': self.nbar})

    def post(self, request, id):
        obj = self.model.objects.get(id=id)
        obj.delete()

        return redirect(reverse(self.redirect_url))