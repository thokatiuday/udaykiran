from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.project)
admin.site.register(models.project_media)
admin.site.register(models.project_skills)
admin.site.register(models.project_points)
admin.site.register(models.social_links)
admin.site.register(models.learning_path)