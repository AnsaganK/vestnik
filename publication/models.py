from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

#class Series(models.Model):
#    name = models.CharField(max_length=100,verbose_name='Название')
#    description = models.TextField(blank=True, verbose_name="Описание")
#    def __str__(self):
#        return self.name
#
#    class Meta:
#        verbose_name = 'Серия'
#        verbose_name_plural = 'Серии'
#
#    def get_absolute_url(self):
#        return reverse('seria_detail',args=[str(self.id)])





class PublicationFiles(models.Model):
    topic = models.CharField(blank=True, max_length=200, verbose_name="Тема")
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name='Автор', related_name='files')
    soauthor = models.TextField(null=True, blank=True, verbose_name="Соавторы")
    comments = models.TextField(null=True, blank=True, verbose_name="Комментарии")
    file = models.FileField(upload_to='all_files', verbose_name="Файл")
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Описание')
    date = models.DateTimeField(auto_now_add=True)
    #series = models.ForeignKey(Series,on_delete=models.CASCADE,related_name='sFiles', verbose_name='Серия')
    vestnik = models.ForeignKey('VestnikFiles',on_delete=models.CASCADE,null=True,blank=True, verbose_name='Относится к вестнику')

    redactor = models.BooleanField(default=False,verbose_name='Редактор')
    redactor_return = models.BooleanField(default=False,verbose_name='Редактор(возврат)')
    redactor_return_text = models.TextField(null=True, blank=True,verbose_name='Редактор(Текст возврата)')
    redactor_error = models.BooleanField(default=False,verbose_name='Редактор(Ошибка)')
    redactor_error_text = models.TextField(null=True, blank=True,verbose_name='Редактор(Текст ошибки)')
    reviewer_choice = models.ManyToManyField(User, blank=True,verbose_name='Рецензенты',related_name='rFiles')

    redactor_update_time = models.DateTimeField(null=True, blank=True)

    antiplagiat = models.BooleanField(default=False,verbose_name='Антиплагиат')
    antiplagiat_point = models.IntegerField(null=True, blank=True,verbose_name='Баллы антиплагиата')
    antiplagiat_file = models.FileField(upload_to='antiplagiat_files',null=True, blank=True,verbose_name='Файл антиплагиата')

    antiplagiat_update_time = models.DateTimeField(null=True, blank=True)

    reviewer = models.BooleanField(default=False,verbose_name='Рецензент')
    reviewer_text = models.TextField(null=True, blank=True, verbose_name='Рецензент(Текст)')
    reviewer_file = models.FileField(upload_to='review_files', null=True, blank=True, verbose_name='Файл рецензента')
    reviewer_return = models.BooleanField(default=False, verbose_name='Рецензент(возврат)')
    reviewer_return_text = models.TextField(null=True, blank=True, verbose_name='Рецензент(Текст возврата)')
    reviewer_error = models.BooleanField(default=False, verbose_name='Рецензент(Ошибка)')
    reviewer_error_text = models.TextField(null=True, blank=True, verbose_name='Рецензент(Текст ошибки)')

    reviewer_update_time = models.DateTimeField(null=True, blank=True)

    payload_img = models.FileField(upload_to='payload_img',null=True, blank=True,verbose_name='Фото оплаты')

    payload = models.BooleanField(default=False,verbose_name='Оплата')

    payload_error = models.BooleanField(default=False,verbose_name='Оплата(Ошибка)')
    payload_error_text = models.TextField(null=True, blank=True,verbose_name='Текст ошибки')

    payload_update_time = models.DateTimeField(null=True, blank=True)

    public = models.BooleanField(default=False,verbose_name='Опубликовать')
    archive = models.BooleanField(default=False, verbose_name='Архив')

    def redactor_date(self, *args, **kw):
        self.redactor_update_time = datetime.now()
        super(PublicationFiles, self).save(*args, **kw)

    def antiplagiat_date(self, *args, **kw):
        self.antiplagiat_update_time = datetime.now()
        super(PublicationFiles, self).save(*args, **kw)

    def reviewer_date(self, *args, **kw):
        self.reviewer_update_time = datetime.now()
        super(PublicationFiles, self).save(*args, **kw)

    def payload_date(self, *args, **kw):
        self.payload_update_time = datetime.now()
        super(PublicationFiles, self).save(*args, **kw)

    def __str__(self):
        return self.author.username+self.topic

    def get_absolute_url(self):
        return reverse('only_publication', args=[str(self.id)])

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

class VestnikFiles(models.Model):
    name = models.CharField(max_length=100,verbose_name="Название вестника")
    year_variants = (
        ('2013', 2013),
        ('2014', 2014),
        ('2015', 2015),
        ('2016', 2016),
        ('2017', 2017),
        ('2018', 2018),
        ('2019', 2019),
        ('2020', 2020),
    )
    month_variants = (
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
        ('6', 6),
        ('7', 7),
        ('8', 8),
        ('9', 9),
        ('10', 10),
        ('11', 11),
        ('12', 12),
    )

    number = models.CharField(max_length=100,null=True,blank=True,verbose_name="Номер вестника")
    year = models.CharField(max_length=4,default=2020,choices=year_variants,verbose_name="Год вестника")
    month = models.CharField(max_length=4,default=1,choices=month_variants,verbose_name="Месяц вестника")

    #current_issue = models.BooleanField(default=False, verbose_name="Текущий выпуск")

    file = models.FileField(upload_to='vestniks', verbose_name="Файл")

    def __str__(self):
        return str(self.name)+str(self.number)+'('+self.year+')'

    def get_name(self):
        return str(self.name)+str(self.number)+'('+self.year+')'

    class Meta:
        verbose_name = "Вестник"
        verbose_name_plural = "Вестники"

class Pages(models.Model):
    title = models.CharField(max_length=30,verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    index = models.IntegerField(default=0)
    basic = models.BooleanField(default=False)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    mobile = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    workPlace = models.TextField(max_length=300, blank=True)
    work = models.TextField(max_length=300, blank=True)
    education = models.CharField(max_length=300, blank=True)
    postCode = models.CharField(max_length=300, blank=True)
    full = models.BooleanField(default=False)
    def full_profile(self, *args, **kw):
        if self.user.first_name and self.user.last_name and self.user.email and self.mobile and self.city and self.birth_date and self.workPlace and self.work and self.education and self.postCode:
            self.full = True
            super(Profile, self).save(*args, **kw)
        else:
            self.full = False
            super(Profile, self).save(*args, **kw)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()