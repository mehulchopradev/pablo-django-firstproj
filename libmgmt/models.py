from django.db import models
from django.urls import reverse

# Create your models here.
class PublicationHouse(models.Model):
    name = models.CharField(max_length=50, null=False)
    ratings = models.IntegerField(null=False)

    # one to many
    # book_set python/django gives it automatically

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50, null=False)
    price = models.FloatField(null=True)
    pages = models.IntegerField(null=False)
    pub_date = models.DateField(null=True)
    count = models.IntegerField(default=0)

    # many to one
    publication = models.ForeignKey(PublicationHouse, on_delete=models.CASCADE, default=None)

    # one to many
    # review_set

    # many to many
    # user_set

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('library:booklist')

class User(models.Model):
    username = models.CharField(max_length=10, null=False)
    password = models.CharField(max_length=20, null=False)
    country = models.CharField(max_length=2, null=False)
    gender = models.CharField(max_length=1, null=False)
    dob = models.DateField(null=False)

    books_issued = models.ManyToManyField(Book)

class Review(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=False)

    # many to one
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
