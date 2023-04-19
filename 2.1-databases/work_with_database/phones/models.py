from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    image = models.URLField(null=True)
    release_date = models.DateField(null=True)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50)

    def __sts__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone ,self).save(*args, **kwargs)