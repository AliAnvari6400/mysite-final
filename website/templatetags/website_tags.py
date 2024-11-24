from django import template
register = template.Library()
from blog.models import Post
from django.utils import timezone

@register.filter
def snippet(value,arg):
    return value[:arg]

@register.inclusion_tag('website/website-latestposts.html')
def latestposts():
    posts = Post.objects.filter(published_date__lte = timezone.now(),status=1).order_by('published_date')[:6]
    return {'posts':posts}
     