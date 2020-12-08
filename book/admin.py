from django.contrib import admin

# Register your models here.
# app/admin.py

from import_export import resources
from import_export.admin import ImportExportModelAdmin,ImportExportActionModelAdmin
from import_export.fields import Field

from .models import Book, Author, Category
class BookResource(resources.ModelResource):
    full_title = Field()

    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'price',)
        export_order = ('id', 'price', 'author', 'name')

    def dehydrate_full_title(self, book):
        return '%s by %s' % (book.name, book.author.name)
# class BookResource(resources.ModelResource):
#     published = Field(attribute='published', column_name='published_date')

#     class Meta:
#         model = Book
        # fields = ('id', 'name', 'author', 'price',)
        # export_order = ('id', 'price', 'author', 'name')

@admin.register(Book)
class BookAdmin(ImportExportActionModelAdmin):
    resources_clasee = BookResource

admin.site.register(Author)
admin.site.register(Category)