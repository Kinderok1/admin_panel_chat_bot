from django.db import models
from django.utils.safestring import mark_safe
from .bot_api.misc.storage_set import get_flag,get_flag_msg

STATUS_SENDLER = [ 'Ждет отправки к ', 'Было отправлено ']



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
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True, verbose_name="Тип")#удалишь тип,удалишь и эти записи

    def baby_boomer_status(self):
        return "what is this"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class MembersList(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    id_s_list = models.CharField(max_length=560, verbose_name='Содержание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Список для рассылки"
        verbose_name_plural = "Списки для рассылки"

class Sendler(models.Model):
    header = models.CharField(max_length=60, verbose_name='Тема')
    text = models.CharField(max_length=360, verbose_name='Содержание')
    members_list = models.ForeignKey(MembersList, on_delete=models.CASCADE, null=True, verbose_name="Список для рассылки")
    send_date = models.DateTimeField(null=True, verbose_name='Время отправки')
    status = models.CharField(max_length=35, null=True, verbose_name='Статус')
    image = models.ImageField(upload_to='sendler_image/', null=True, blank=True, verbose_name='Изображение')

    def save(self, *args, **kwargs):
        """
        Надстройка перед сохранением
        """
        send_date = str(self.send_date)[:19]
        self.status = STATUS_SENDLER[0] + send_date
        super().save(*args, **kwargs)
        #тут хорошо бы сделать какой нибудь хук,наверное...


        flag=dict()
        flag['date'] = send_date
        flag['caption'] = self.header
        flag['status'] = STATUS_SENDLER[1]
        flag['pk'] = self.pk
        get_flag(flag)

    def __str__(self):
        return self.header

    def image_tag(self):
        return mark_safe('<img src="%s" width="105" height="105" />' % (
            self.image.url))  # Get Image url
    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"

class Notifications(models.Model):
    from_user_name = models.CharField(max_length=70,blank=True,null=True)
    from_user_id = models.IntegerField(null=True, blank=True)
    is_read = models.BooleanField(default=False)
    url_to_dialog = models.CharField(max_length=50,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']

class Messages(models.Model):
    owner = models.ForeignKey(Members, on_delete=models.CASCADE)
    from_user_msg = models.CharField(max_length=4095,null=True, blank=True)
    to_user_msg = models.CharField(max_length=4095,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def save(self, *args, **kwargs):
        """
        Надстройка перед сохранением
        """
        super().save(*args, **kwargs)

        if self.to_user_msg:
            flag = dict()
            flag['msg'] = self.to_user_msg
            flag['owner'] = self.owner
            get_flag_msg(flag)



