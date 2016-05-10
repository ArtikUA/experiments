from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView


class MyView(TemplateView):
    template_name = '1.html'

    def get_context_data(self, article_id):
        context = super(MyView, self).get_context_data()
        print(context)
        print(self)
        context['foo'] = article_id
        return context


class RedView(RedirectView):
    def get_redirect_url(self, id):
        id = id
        return reverse('article-detail', kwargs={'article_id': id})
