from django.urls import path
from main_app.views import ApplicationListView, ApplicationDetailView, ApplicationCreateView, ApplicationUpdateView
from django.views.generic import TemplateView

urlpatterns = [
    path('app/', ApplicationListView.as_view(), name='application'),
    path('app/<int:pk>/', ApplicationDetailView.as_view(), name='application-detail'),
    path('app/add/', ApplicationCreateView.as_view(), name='application-add'),
    path('app/<int:pk>/update', ApplicationUpdateView.as_view(), name='application-update'),
    path('', TemplateView.as_view(template_name='base.html'), name='index')
]
