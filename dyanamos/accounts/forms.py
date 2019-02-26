from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import (
    User, UploadGamePromo,FanOfTheMatch,
    ManOfTheMatch,TravelWithTheTeam,MomementOfTheMatch,
)

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username","first_name","last_name","identification_number","password1", "password2")
        labels = {
            'username': _('phone number'),
        }
class UploadGamePromoForm(ModelForm):
    class Meta:
        model = UploadGamePromo
        fields = ['team_one', 'team_two', 'match_image', 'date_played']
        labels = {
            'team_one': _('Enter team playing at home'),
            'team_two': _('Enter team playing at away'),
        }

class FanOfTheMatchForm(ModelForm):
    class Meta:
        model = FanOfTheMatch
        fields = ['name_of_fan','fan_image','published']
        labels = {
            'name_of_fan': _('Name of the Fan or any caption'),
            'fan_image': _('Upload Image'),
        }


class ManOfTheMatchForm(ModelForm):
    class Meta:
        model = ManOfTheMatch
        fields = ['name_of_man_of_the_match','man_of_the_match_image','published']
        labels = {
            'name_of_man_of_the_match': _('Name of Man of the Match'),
            'man_of_the_match_image': _('Upload Image'),
        }

class TravelWithTheTeamForm(ModelForm):
    class Meta:
        model = TravelWithTheTeam
        fields = ['team_caption','best_team_image','published']
        labels = {
            'team_caption': _('Best travel with the team image'),
            'best_team_image ': _('Upload Image'),
        }


class MomementOfTheMatchForm(ModelForm):
    class Meta:
        model = MomementOfTheMatch
        fields = ['name_of_the_moment','image_of_the_moment','published']
        labels = {
            'name_of_the_moment': _('Best travel with the team image'),
            'image_of_the_moment ': _('Upload Image'),
        }


