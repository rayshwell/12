# 使用django框架中集成的RSS包装工具
from django.contrib.syndication.views import Feed
from .models import Article
from django.shortcuts import reverse,redirect
class ArticleFeed(Feed):
    title="Web全栈开发技术"
    description="定期发布一系列Web全栈开发"
    link ="/"
    def items(self):
        return Article.objects.all().order_by("-create_ime")
    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.author
    def item_link(self, item):
        url=reverse('blogapp:detail',args=(item.id,))
        return url