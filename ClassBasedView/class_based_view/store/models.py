from django.db import models



class BaseModel(models.Model):
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()

    class Meta:
        abstract = True


class Books(BaseModel):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 1020)
    price = models.IntegerField()

    class Meta:
        db_table = 'books'


class PicturesManager(models.Manager):
    def filter_by_book(self, book):
        return self.filter(book=book).all()



class Pictures(BaseModel):

    picture = models.FileField(upload_to='picture/')
    book = models.ForeignKey(
        'books', on_delete=models.CASCADE
    )
    objects = PicturesManager()