from django.contrib import admin
from Blog.models import ArticlePost
from Blog.models import BlogUser,Banner,BlogCategory,Tag,EmailVerifyRecord
# from Blog.models import Banner, EmailVerifyRecord
# Register your models here.
# class Tagmodels(admin.ModelAdmin):
#     list_display = ['name']


class ArticlePostModel(admin.ModelAdmin):
    list_display = ['author', 'created','title','title_imgs', 'excerpt','body','updated']


# class Categorys(admin.ModelAdmin):
#     list_display = ['name']

admin.site.register(Tag)
admin.site.register(BlogUser)
admin.site.register(BlogCategory)
admin.site.register(ArticlePost, ArticlePostModel)
admin.site.register(Banner)
admin.site.register(EmailVerifyRecord)
