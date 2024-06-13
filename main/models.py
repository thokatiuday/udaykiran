from django.db import models

# Create your models here.
class project(models.Model):
    project_id = models.CharField(max_length=120)
    project_name = models.CharField(max_length=200)
    deployed_link = models.URLField(blank=True,null=True)
    github_link = models.URLField()
    description = models.TextField()
    short_description = models.CharField(max_length=120,blank=True,null=True)
    
    def __str__(self) -> str:
        return self.project_id

class project_media(models.Model):
    project_id = models.ForeignKey(project,on_delete=models.CASCADE)  
    image = models.ImageField(upload_to='project/')
    
    def __str__(self) -> str:
        return self.project_id.project_id
    
class project_skills(models.Model):
    project_id = models.ForeignKey(project,on_delete=models.CASCADE)
    skills_used = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f'{self.skills_used} for {self.project_id.project_id}'
    
class project_points(models.Model):
    project_id = models.ForeignKey(project,on_delete=models.CASCADE)
    key_points = models.TextField()
    
    def __str__(self) -> str:
       return f'{self.project_id.project_id} --> {self.key_points[0:30]}'

class social_links(models.Model):
    link_logo = models.CharField(max_length=100)
    link = models.URLField()
    
    def __str__(self) -> str:
        return f'{self.link_logo} -> {self.link}'
    
class learning_path(models.Model):
    date = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return f'{self.date} to {self.message}'