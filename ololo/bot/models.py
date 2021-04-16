from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Members(models.Model):
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    id_t = models.CharField(max_length=60, verbose_name='Телеграм ID',default='12378')
    name = models.CharField(max_length=110, verbose_name='ИМЯ',default='Pavel')
    def image_tag(self):
        return mark_safe('<img src="%s" width="90" height="90" />' % (
            self.image.url))  # Get Image url
    class Meta:
        verbose_name = "Подписчика"
        verbose_name_plural = "Подписчики"

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