from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.

User=get_user_model()

class Students(models.Model):
    slug= models.SlugField(allow_unicode=True,unique=True)
    user=models.ForeignKey(User, related_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug= slugify(self.name)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('students:single', kwargs={'slug':self.slug,
                                                  'username':self.user.username})
