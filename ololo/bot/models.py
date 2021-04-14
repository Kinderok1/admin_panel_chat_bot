from django.db import models

# Create your models here.
class Type(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Items(models.Model):
    caption = models.CharField(max_length=60, verbose_name='Название товара')
    image = models.CharField(max_length=10, verbose_name='Изображение')
    description = models.CharField(max_length=150, verbose_name='Описание товара')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True, verbose_name="Тип")

    def baby_boomer_status(self):
        return "what is this"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"