from django.urls import path, re_path
from nav.views import MyView, About, Test, Testing, minimize
from django.conf import settings

urlpatterns = [
    re_path('^$', MyView.as_view(), name='my-view'),
    path('about',About.as_view(), name='about-view'),
    path('test', Test.as_view(), name='test-view'),
    path('testing', Testing.as_view(), name='testing-view'),
    path('minimize',minimize.as_view(),name='minimize-view')
]