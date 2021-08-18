from django.shortcuts import render, get_object_or_404
from django.views.generic import  ListView, DetailView
from django.core.paginator import Paginator
from .models import Article, Category

#new one
class ArticleList(ListView):
    #model = Article
    queryset = Article.objects.published()
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 2


class ArticleDetail(DetailView):
    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article, slug=slug, status="p")
    template_name = 'blog/detail.html'


class CategoryList(ListView):
    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context

    context_object_name = 'articles'
    template_name = 'blog/category.html'
    paginate_by = 2




# def home(request, page=1):
#     articles_list = Article.objects.all()
#     paginator = Paginator(articles_list, 2)
#     articles = paginator.get_page(page)
#     context = {'posts': articles,
#                'category': Category.objects.filter(status=True)
#
#                }
#     return render(request, 'blog/home.html', context)


# def detail(request, slug):
#     context = {'article': get_object_or_404(Article, slug=slug, status="p"),
#                'category': Category.objects.filter(status=True)
#
#                }
#     return render(request, 'blog/detail.html', context)


# def category(request, slug, page=1):
#     category = get_object_or_404(Category, slug=slug, status=True)
#     articles_list = category.articles.published()
#     paginator = Paginator(articles_list, 2)
#     articles = paginator.get_page(page)
#     context = {'category': get_object_or_404(Category, slug=slug, status=True),
#                'articles': articles
#                }
#     return render(request, 'blog/category.html', context)


