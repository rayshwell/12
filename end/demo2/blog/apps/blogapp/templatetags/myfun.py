from django.template import Library
from ..models import Article,Category,Tag
register=Library()

@register.filter
def dataFormat(data):
    return "%d-%d-%d"%(data.year,data.month,data.day)
@register.filter
def authorFormat(author,info):
    return info+":"+author
@register.simple_tag
def get_latestarticles(num=3):
    return Article.objects.all().order_by("-create_ime")[:num]
@register.simple_tag
def get_latesdates(num=3):
                                 # field_name  kind  order
    dates=Article.objects.dates("create_ime","month","DESC")[:num]
    return dates
@register.simple_tag
def get_categorys(num=3):
    return Category.objects.all().order_by("id")[:num]
@register.simple_tag
def get_tags(num=3):
    return Tag.objects.all().order_by("id")[:num]