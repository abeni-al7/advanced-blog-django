from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from taggit.models import Tag
from .models import Post


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated


class TagSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        # Get tags used in published posts
        return Tag.objects.filter(
            pk__in=Post.published.values_list("tags", flat=True)
        ).distinct()

    def location(self, tag):
        return reverse("blog:post_list_by_tag", kwargs={"tag_slug": tag.slug})

    # Optional: Add last modification date (using latest post's update time)
    def lastmod(self, tag):
        latest_post = Post.published.filter(tags=tag).order_by("-updated").first()
        return latest_post.updated if latest_post else None
