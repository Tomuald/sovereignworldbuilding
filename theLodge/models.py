from django.db import models
from django.urls import reverse

from accounts.models import CustomUser
from ItemList.models import Itemlist

class AbstractSharedObject(models.Model):
    name = models.CharField(max_length=255, unique=True)
    game_system = models.CharField(max_length=255)

    description = models.TextField()

    shared_at = models.DateField(auto_now_add=True)
    shared_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def get_absolute_url(self):
        return reverse('shared-itemlist', args=[str(self.id)])

class SharedItemlist(AbstractSharedObject):
    itemlist = models.ForeignKey(Itemlist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
