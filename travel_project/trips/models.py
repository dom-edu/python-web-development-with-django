from django.db import models

# Create your models here.

# Exercise: Making A Trip Model: (What goes into making a trip, Include a Image for uploading. )

# Requirements:include an image field and any other fields you see fit!  

class Trip(models.Model):
    title = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    # date time field 
    start_date = models.DateField()
    end_date = models.DateField()

    #
    image = models.ImageField(upload_to='destinations/')
    # auto generated 
    created_at = models.DateTimeField(auto_now_add=True)


    # sql table attributes 
    class Meta():

        # when you sort by multiple things 
        # weak ordering. First order-> date, title -> second order 
        ordering = ['-start_date', 'title']

    def __str__(self):
        return f"{self.title} - {self.location}"
    

