from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('lda',views.lda, name='lda'),
    # path('awshaf', views.lda , name='awshaf')
]