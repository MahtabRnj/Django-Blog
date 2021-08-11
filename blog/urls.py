from silisPro.settings import DEBUG
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('', views.ArticleList.as_view(), name='blog_home'),
    path('page/<int:page>', views.ArticleList.as_view(), name='blog_home'),
    path('article/<slug:slug>', views.ArticleDetail.as_view(), name='blog_detail'),
    path('category/<slug:slug>', views.CategoryList.as_view(), name='blog_category'),
    path('category/<slug:slug>/post/<int:page>', views.CategoryList.as_view(), name='blog_category')
]

if DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
