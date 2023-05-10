from django.contrib import admin
from .models import Author, Book, Genre, Language, Status, BookInstance

admin.site.register(Author)


# class AuthorAdmin(admin.ModelAdmin):
#     # List_display =('last_name', 'first_name')
#     # fields = ['last_name', 'first_name', ('date_of_birth', 'date_of_death')]
#
#
# admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)


# class BookAdmin(admin.ModelAdmin):
#     List_display =('title', 'genre', 'language', 'display_author')
#     List_filter = ('genre', 'author')


# admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
admin.site.register(BookInstance)


# @admin.register(BookInstance)
# class BookInstanceAdmin(admin.ModelAdmin):
#     # List_filter = ('book', 'status')
#     # fieldsets = (
#     #     ('Экземпляр книги', {
#     #         'fields': ('status', 'imprint', 'inv_nom')
#     #     }),
#     #     ('Статус и окончание его действия', {
#     #         'fields': ('status', 'due_back')
#     #     })
#     # )


# Register your models here.
