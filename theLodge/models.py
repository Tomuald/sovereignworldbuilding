from django.db import models
from django.urls import reverse

from accounts.models import CustomUser
from Project.models import Project
from ItemList.models import Itemlist
from World.models import Universe

class AbstractSharedObject(models.Model):
    name = models.CharField(max_length=255, unique=True)
    game_system = models.CharField(max_length=255)

    description = models.TextField()

    shared_at = models.DateField(auto_now_add=True)
    shared_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class SharedItemlist(AbstractSharedObject):
    itemlist = models.ForeignKey(Itemlist, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('shared-itemlist', args=[str(self.id)])

    def __str__(self):
        return self.name

class SharedProject(AbstractSharedObject):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('shared-project', args=[str(self.id)])

    def __str__(self):
        return self.name

class SharedUniverse(AbstractSharedObject):
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('shared-universe', args=[str(self.id)])

    def __str__(self):
        return self.name
