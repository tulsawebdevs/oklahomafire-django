from django.conf.urls.defaults import *
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="oklahomafire/index.html"), name="firehome"),
    url(r'^all/$', 'oklahomafire.views.firedata', name='firedata'),
)
