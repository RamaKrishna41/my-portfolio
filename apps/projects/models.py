from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)    # Project name
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title