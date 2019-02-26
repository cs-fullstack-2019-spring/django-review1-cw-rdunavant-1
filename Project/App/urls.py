from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    # path('<int:page_id>/', views.page2, name='page2'),
    # path('<int:page_id>/', views.page3, name='page3'),
    # path('<int:page_id>/', views.page4, name='page4'),
    # path('<int:page_id>/', views.page5, name='page5'),
]