from django.conf.urls import patterns, include, url
from LinguisticSuggestion.views import consumer as cs
from LinguisticSuggestion.views import producer as pd
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'cs/index/', cs.Index.as_view()),
    url(r'pd/index/', pd.Index.as_view()),

    url(r'get_suggest/', cs.GetSuggestions.as_view()),
    url(r'get_result/', cs.GetResult.as_view()),
    url(r'get_operators/', cs.GetOperators.as_view()),

    url(r'build_suggest_operator_index/', pd.GetSuggestions.as_view()),
    url(r'get_result/', cs.GetResult.as_view()),
    url(r'get_operators/', cs.GetOperators.as_view()),
)
