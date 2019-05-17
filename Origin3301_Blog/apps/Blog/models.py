# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
import datetime
from django.db.models import Q


class BlogUser(User):
    nikename = models.CharField('昵称', max_length=20, default='')


# 博客分类
class BlogCategory(models.Model):
    blog_tyle = models.CharField("分类", max_length=128)
    class Meta:
        db_table = "Categorys"
        verbose_name = "博客分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.blog_tyle


# 标签
class Tag(models.Model):
    name = models.CharField('标签', max_length=128)
    class Meta:
        db_table = "Tag"
        verbose_name = '博客标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章
class ArticlePost(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    author = models.ForeignKey(BlogUser, on_delete=models.CASCADE, verbose_name="作者")
    category = models.ForeignKey(BlogCategory,verbose_name="博客分类",blank=True, null=True,on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag,verbose_name="标签")
    title = models.CharField(max_length=80, verbose_name="标题")
    title_imgs = models.ImageField(null=True,blank=True,upload_to='Cover/',verbose_name='博客封面')
    excerpt = models.CharField(max_length=250, blank=True, verbose_name='摘要')
    body = RichTextUploadingField(config_name='my_config')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    visiting = models.PositiveIntegerField('浏览数', default=0)
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'ArticlePost'
        ordering = ('-created',)
        verbose_name = '博客'
        verbose_name_plural = verbose_name


# 轮播图
class Banner(models.Model):
    title = models.CharField('标题', max_length=50)
    cover = models.ImageField('轮播图', upload_to='Bnaner')
    link_url = models.URLField('图片链接',max_length=100)
    idx = models.IntegerField('索引')
    is_active = models.BooleanField('是否active', default=False)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'


# 评论
# class Comment(models.Model):
#     post = models.ForeignKey(ArticlePost, verbose_name='博客')
#     user = models.ForeignKey(BlogUser, verbose_name='作者')
#     pub_date = models.DateTimeField('发布时间')
#     content = models.TextField('内容')
#
#     def __str__(self):
#         return self.content
#     class Meta:
#         verbose_name = '评论'
#         verbose_name_plural = '评论'

# Email(邮箱验证数据模型)
class EmailVerifyRecord(models.Model):
    code = models.CharField(verbose_name='验证码', max_length=50,default='')
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(verbose_name="验证码类型", choices=(("register",u"注册"),("forget","找回密码"), ("update_email","修改邮箱")), max_length=30)
    send_time = models.DateTimeField(verbose_name="发送时间", default=datetime.timezone)

    class Meta:
        verbose_name = "邮箱验证码"
        # 复数
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset()\
                        .filter(status='published')

class Post(models.Model):
    object = models.Manager() # The default manager
    published = PublishedManager() # Our custom manager