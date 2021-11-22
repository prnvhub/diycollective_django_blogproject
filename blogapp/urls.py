from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='hm'),
    path('dash/',views.dash,name='dash'),
    path('posts/',views.post_create,name='post_create'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('single/<int:id>',views.single,name='single'),
]