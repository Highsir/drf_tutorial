from django.db import models
from datetime import datetime


class FileSys(models.Model):
    filename = models.CharField(max_length=64)
    uploader = models.CharField(max_length=20)
    file_size = models.IntegerField(max_length=4)
    first_upload_time = models.DateTimeField()
    last_upload_time = models.DateTimeField()


class Comment(models.Model):
    email = models.EmailField()
    content = models.CharField(max_length=200)
    created = models.DateTimeField(default=datetime.now())


class Topping(models.Model):
    name = models.CharField(max_length=30)


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return "%s (%s)" % (
            self.name,
            ", ".join(topping.name for topping in self.toppings.all()),
        )


class Restaurant(models.Model):
    pizzas = models.ManyToManyField(Pizza, related_name='restaurants')
    best_pizza = models.ForeignKey(Pizza, related_name='championed_by', on_delete=models.CASCADE)


class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)
    pub_date = models.DateTimeField(default=datetime.now())
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline
