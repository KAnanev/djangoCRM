from django.views.generic import ListView, DetailView
from main_app.models import Application
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ApplicationListView(LoginRequiredMixin, ListView):
    model = Application

    def get_queryset(self):
        queryset = super(ApplicationListView, self).get_queryset()
        queryset = queryset.filter(client=self.request.user)
        return queryset


class ApplicationDetailView(UserPassesTestMixin, DetailView):
    model = Application

    def test_func(self):
        queryset = super(ApplicationDetailView, self).get_queryset()
        queryset = queryset.filter(pk=self.kwargs['pk'])
        return str(queryset[0].client) == str(self.request.user.username)


class ApplicationCreateView(LoginRequiredMixin, CreateView):
    login_url = '/app'
    model = Application
    fields = ['title', 'text', 'type_app']

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)


class ApplicationUpdateView(LoginRequiredMixin, UpdateView):
    model = Application
    fields = ['title', 'text', 'status', 'type_app']
