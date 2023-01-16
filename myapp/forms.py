from django.contrib.auth.forms import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from myapp.models import Movie, Show, Payment


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'email'
        ]


class MovieAddForm(forms.ModelForm):
    class Meta:
        Model = Movie
        fields = [
            'movie_id',
            'movie_name',
            'duration',
            'start_date',
            'end_date'
        ]


class ShowAddForm(forms.ModelForm):
    class Meta:
        Model = Show
        fields = [
            'show_id',
            'show_time',
            'show_date',
            'movie'
        ]


class PaymentForm(forms.ModelForm):
    class Meta:
        Model = Payment
        fields = [
            'payment_id',
            'booking',
            'method',
            'customer',
            'amount'
        ]
