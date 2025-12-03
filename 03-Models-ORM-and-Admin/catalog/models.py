from django.db import models

# Create your models here.
# each represent a table in the database 
# mapping classes onto db tables is what is meant by ORM 
# Object Relational Mapping 

# way better than writing some SQL which would be 
# CREATE TABLE Genre(VarChar(100))
class Genre(models.Model):
    """ Model representing a book's genre. (EX: fiction, sci-fi.) """
    name = models.CharField(max_length=100, unique=True)


    "Model metadata is “anything that’s not a field”, such as ordering options (ordering), database table name (db_table), or human-readable singular and plural names (verbose_name and verbose_name_plural). None are required, and adding class Meta to a model is completely optional."
    class Meta:

        # this orders the table lexicographically on the DB Side
        ordering = ["name"]

    def __str__(self):
        # string reprensentation of the object 
        # every object in python has __str__
        return self.name
    
class Author(models.Model):
    """ Model representing a book's author. """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_year = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ["last_name", "first_name"]
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Book(models.Model):
    """ Model representing a book's information with relationships to author and genre data. """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    genre = models.ManyToManyField(Genre, related_name="books")
    publication_year = models.IntegerField()
    isbn = models.CharField("ISBN", max_length=13, unique=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
