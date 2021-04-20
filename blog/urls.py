from django.urls import path
from . import views


urlpatterns = [
    # POST CRUD Operations 
    path('create/',views.create_view, name = 'create-path'),
    path('',views.list_view, name = 'home-path'),
    path('list/<int:post_pk>',views.detail_view, name = 'detail-path'),
    path('update/<int:post_pk>',views.update_view, name = 'update-path'),
    path('delete/<int:post_pk>',views.delete_view, name = 'delete-path'),

     # Contribution CRUD Operations 

    path('contributioncreate/<int:post_pk>',views.contributioncreate_view, name = 'contributioncreate-path'),
    path('contributionlist/<int:post_pk>',views.contributionlist_view, name = 'contributionlist-path'),
    #path('contributionupdate/<int:contrib_pk>',views.contributionupdate_view, name = 'contributionupdate-path'),
    # path('contributidelete/<int:contributi_pk>',views.contributidelete_view, name = 'contributidelete-path'),

]

