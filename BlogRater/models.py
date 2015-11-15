from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.CharField(max_length=128, unique=True, primary_key=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.id

# from BlogRater.models import Category
# c = Category(id="1",rating=0)
# c.save()
# print Category.objects.all()
# quit()