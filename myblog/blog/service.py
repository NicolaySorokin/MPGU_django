from django.db.models import Count
from django.utils import timezone

from blog.models import Post


def profile_posts(
    filter_published=False,
    count_comment=True,
    queryset=None
):
    queryset = queryset or Post.objects

    if count_comment:
        queryset = queryset.annotate(comment_count=Count('comments'))

    queryset = queryset.select_related(
        'category', 'author', 'location'
    )

    if filter_published:
        queryset = queryset.filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now()
        )

    return queryset.order_by('-pub_date')
