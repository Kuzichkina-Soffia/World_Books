from django.db import models
from django.urls import reverse

# Create your models here.


class Genre (models.Model):
    name = models.CharField(max_length=200,
    help_text=" введите жанр книги",
    verbose_name="жанр книги")

    def __str__(self):
        return self.name


class Language (models.Model):
    name = models.CharField(max_length=20,
    help_text =" введите язык книги",
    verbose_name = "язык книги")


class Author (models.Model):
    first_name = models.CharField(max_length=100,
                                    help_text =" введите имя автора",
                                    verbose_name = "имя автора")
    last_name = models.CharField(max_length=100,
                                    help_text =" введите фамилию автора",
                                    verbose_name = "фамилия автора")
    date_of_birth = models.DateField(
                                    help_text =" введите дату рождения автора",
                                    verbose_name = "дата рождения автора",
                                    null=True, blank=True)
    date_of_death = models.DateField(
                                    help_text =" введите дату смерти автора",
                                    verbose_name = "дата смерти автора",
                                    null=True, blank=True)
    def __str__(self):
        return self.last_name


class Book (models.Model):
    title = models.CharField(max_length=200,
                                    help_text ="Введите название книги",
                                    verbose_name = "название книги")
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE,
                                    help_text =" выберите жанр книги",
                                    verbose_name = "Жанр книги", null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE,
                                    help_text =" выберите язык книги",
                                    verbose_name = "язык книги",null=True)
    author = models.ManyToManyField('Author',
                                    help_text ="Выберите автора книги",
                                    verbose_name = "автор книги")
    summary = models.TextField(max_length=1000,
                                    help_text ="Введите краткое описание книги",
                                    verbose_name = "Аннотация книги")
    isbn = models.CharField(max_length=13,
                                    help_text = "Должно содержать 13 символов",
                                    verbose_name = "ISBN книги")
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def display_author(self):
        return ', '.join([author.last_name for author in self.author.all()])
    display_author.short_description = 'Авторы'

class Status (models.Model):
    name = models.CharField(max_length=50,
    help_text =" введите статус книги",
    verbose_name = "статус экземпляра книги")

    def __str__(self):
        return self.name


class BookInstance (models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    inv_nom= models.CharField(max_length=20, null=True,
                                    help_text ="Введите инвентарный номер экземпляра",
                                    verbose_name = "Инвентарный номер")
    imprint = models.CharField(max_length=200,
                                    help_text ="введите издательство и год выпуска",
                                    verbose_name = "издательство")
    status = models.ForeignKey('Status', on_delete=models.CASCADE, null=True,
                                    help_text ="Изменить сотояние экземпляра",
                                    verbose_name = "Статус экземпляра книги")
    def_back = models.DateField(null=True, blank=True,
                                    help_text ="Введите конец срока статуса",
                                    verbose_name = "дата окончания статуса")
    def __str__(self):
        return '%s %s %s' % (self.inv_nom, self.book, self.status)