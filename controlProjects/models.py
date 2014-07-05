from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class GoalLight(models.Model):
    user = models.OneToOneField(User)
    lightOn = models.BooleanField(default=True)
    soundOn = models.BooleanField(default=False)
    onTime = models.IntegerField(default=10)
    #onNow = models.IntegerField(default=False)
    
    def __unicode__(self):
        returnString = "%sLight" % unicode(self.user)
        return returnString
    
    
