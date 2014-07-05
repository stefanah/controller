##from login.models import UserProfile
##from django.contrib.auth.models import User
from django import forms
from models import GoalLight
from django.contrib.auth.models import User


class GoalLightForm(forms.ModelForm):
    def __init__(self, user, goal, *args, **kwargs):
        super(GoalLightForm, self).__init__(*args, **kwargs)
        self.user = user
        print "\n", user, "User passed to GoalLightForm", goal.id
        #self.fields['used_his'].queryset = User.objects.filter(pk = user.id)
    onTime = forms.IntegerField(initial=10)
    lightOn = forms.BooleanField(initial=True, required=False)
    soundOn = forms.BooleanField(initial=False, required=False)
    
    class Meta:
        model = GoalLight
        exclude = ('user', 'timer',)  #uncomment once user is set automatically
        fields = ('onTime', 'lightOn', 'soundOn')
        
        #fields = ('timer', 'lightOn', 'soundOn', 'user')