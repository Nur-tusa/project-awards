from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Project(models.Model):
    img = models.ImageField(default='default.png', upload_to='images')
    title = models.CharField(default='My Project', max_length = 40)
    description = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    reviews = models.CharField(max_length = 40, blank = True, default = 0)
    link = models.CharField(default='No link', max_length = 120)
    av_usability = models.CharField(max_length = 40, default = 0)
    av_design = models.CharField(max_length = 40, default = 0)
    av_content = models.CharField(max_length = 40, default = 0)
    rating = models.CharField(max_length = 40, default = 0)

    def __str__(self):
        return self.title

    @classmethod
    def search_by_title(cls,search_term):
        projectis = cls.objects.filter(title__icontains=search_term)
        return projectis

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})


    def get_project_by_id(project_id):
        project = Project.objects.get(pk = project_id)
        return project