from django.db import models
from django.utils.text import slugify

class Idea(models.Model):
    class Meta:
        ordering = ('-created_at',)
    
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(unique=True, max_length=200)
    description = models.TextField(null=True, blank=True)
    external_link = models.URLField(null=True, blank=True)
    internal_link = models.URLField(null=True, blank=True)
    submitted_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    magnitude = models.IntegerField(default=1)
    slug = models.SlugField(unique=True, editable=False)


    def __str__(self):
        return self.title
    
    def save(self, *args, keep_slug=False, **kwargs):
        if not keep_slug: 
            self.slug = slugify(self.title)
        self.validate_unique()
        return super().save(*args, **kwargs)