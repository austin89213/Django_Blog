from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin,ImportExportActionModelAdmin
from import_export.fields import Field

from . models import Post, Comment
# Register your models here.



class PostResource(resources.ModelResource):
    full_title = Field()

    class Meta:
        model = Post

    def dehydrate_full_title(self, book):
        return '%s by %s' % (Post.titel, Post.author)


@admin.register(Post)
class PostAdmin(ImportExportActionModelAdmin):
    resources_clasee = PostResource


class CommentResource(resources.ModelResource):

    class Meta:
        model = Comment
        

@admin.register(Comment)
class CommentAdmin(ImportExportActionModelAdmin):
    resources_clasee = CommentResource