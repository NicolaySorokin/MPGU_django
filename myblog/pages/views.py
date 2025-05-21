from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView

from .models import StaticPage


class StaticPageView(DetailView):
    model = StaticPage
    template_name = 'pages/static.html'
    context_object_name = 'page'

    def get_object(self, queryset=None):
        return get_object_or_404(StaticPage, slug=self.kwargs['slug'])


def custom_404(request, exception=None):
    return render(request, 'pages/404.html', status=404)


def custom_500(request):
    return render(request, 'pages/500.html', status=500)


def custom_403(request, exception=None):
    return render(request, 'pages/403csrf.html', status=403)
