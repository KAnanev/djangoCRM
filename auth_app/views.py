from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import UserRegistrationForm
from django.views.generic.detail import DetailView
from auth_app.models import User
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound


def redirect_to_user_page(request):
    user_id = request.user.pk
    return redirect(reverse('profile', kwargs={"pk": user_id}))


def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            user_form = UserRegistrationForm(request.POST)
            if user_form.is_valid():
                new_user = user_form.save(commit=False)
                new_user.set_password(user_form.cleaned_data['password'])
                new_user.save()
                return render(request, 'registration/register_done.html', {'new_user': new_user})

        user_form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'user_form': user_form})
    return redirect_to_user_page(request)


class UserView(DetailView, LoginRequiredMixin):
    model = User

@csrf_exempt
def get_telegram_id(request):

    if request.method == 'POST':
        try:
            token = request.GET.get('token')
            user = User.objects.get(user_token=token)
            telegram_id = request.GET.get('telegram_id')
            print(telegram_id)
            user.telegram_id = int(telegram_id)
            user.save()
            return HttpResponse('Оповещение включено!')

        except User.DoesNotExist:
            return HttpResponseNotFound("Не найден юзер!")
