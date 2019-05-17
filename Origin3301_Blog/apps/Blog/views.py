from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from Blog.models import ArticlePost
from Blog.models import BlogUser,Banner,BlogCategory,Tag,EmailVerifyRecord
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
import markdown
from django.db.models import Q


def post_list(request):

    page_list = ArticlePost.objects.all()
    new_article = ArticlePost.objects.all().order_by('-id')[:3]
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(page_list, per_page=5, request=request)
    page_list = p.page(page)

    ctx = {
        'page_list': page_list,
        'new_article': new_article,
    }
    return render(request, 'blog/index.html', ctx)


def article_detail(request,id):
    article = ArticlePost.objects.get(id=id)
    # 浏览数
    article.visiting += 1
    article.save(update_fields=['visiting'])
    context = {'article': article}
    return render(request, 'blog/detail.html', {'article': article})


def search_tag(request, tag):
    try:
        tag_list = ArticlePost.objects.filter(tags=tag)
    except ArticlePost.DoesNotExist:
        raise get_object_or_404
    return render()


# def banner(request):
#     banner_list = Banner.objects.all()
#     ctx = {
#         'banner_list':banner_list,
#     }
#     return render(request,'Banner.html', ctx)



# markdown
# def index(request, id):
#     article = ArticlePost.objects.get(id=id)
#
#     # 将markdown语法渲染成html样式
#     article.body = markdown.markdown(article.body,
#          extensions=[
#              # 包含 缩写、表格等常用拓展
#              'markdown.extensions.extra',
#              # 语法高亮
#              'markdown.extensions.codehilite',
#          ])
#
#     # context = {'article': article}
#     return render(request, 'blog/index.html',{'article': article})