from django.db import models

# Create your models here.

class Jobs(models.Model):
    name = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True)
    
    class Meta:
        verbose_name_plural = "Jobs"

    def __unicode__(self):
        return '%s' % (self.name)


class Member(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, unique=True, null=True)
    
    class Meta:
        verbose_name_plural = "Member"

    def __unicode__(self):
        return '%s' % (self.name)
