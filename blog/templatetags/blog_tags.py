from django import template
register = template.Library()
from blog.models import Post,Category
from django.utils import timezone

@register.filter
def snippet(value,arg):
    return value[:arg]

@register.inclusion_tag('blog/blog_latestposts.html')
def latestposts():
    posts = Post.objects.filter(published_date__lte = timezone.now(),status=1).order_by('published_date')[:2]
    return {'posts':posts}

@register.inclusion_tag('blog/blog_postcategories.html')
def postcategories():
    posts = Post.objects.filter(published_date__lte = timezone.now(),status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories':cat_dict}     

@register.inclusion_tag('blog/blog-tag-clouds.html')
def tagclouds():
    posts = Post.objects.filter(published_date__lte = timezone.now(),status=1)
    tags=set()
    for post in posts:
        post_all_tags = post.tags.all()
        for i in range(len(post_all_tags)):
            tags.add(post_all_tags[i])
    #print(tags)
    return {'tags':tags}