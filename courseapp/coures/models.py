from django.db import models
from django.contrib.auth.models import AbstractUser
<<<<<<< HEAD


class User(AbstractUser):
    pass


class BaseModel(models.Model):
    created_date = models.DateField(auto_now_add=True, null=True)
    updated_date = models.DateField(auto_now=True, null=True)
=======
class User(AbstractUser):
    pass

class BaseModel(models.Model):
    created_date = models.DateField(auto_now_add=True, null = True)
    updated_date = models.DateField(auto_now=True, null = True)
>>>>>>> origin/main
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(BaseModel):
<<<<<<< HEAD
    name = models.CharField(max_length=50, null=False)
=======
    name = models.CharField(max_length=50, null = False)
>>>>>>> origin/main

    def __str__(self):
        return self.name


class Course(BaseModel):
<<<<<<< HEAD
    subject = models.CharField(max_length=255, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.subject

    class Meta:
        unique_together = ('subject', 'category')


class Lesson(BaseModel):
    subject = models.CharField(max_length=255, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to='Lesson/%Y/%m')
    course = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')

    class Meta:
        unique_together = ('subject', 'course')


class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)
=======
    subject = models.CharField(max_length=255, null = False)
    description = models.TextField()
    image = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject
>>>>>>> origin/main
# Create your models here.
