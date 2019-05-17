from django.urls import path
from Blog import views

# urlpatterns = [
#     path("add_tltle", views.add_title, ),
#     path('show_title', views.show_title, ),
# ]

urlpatterns = [
    path('',views.post_list, name='psot_list'),
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
]