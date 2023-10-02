from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('',views.index,name='index'),
    path('items/',views.item,name='item'),
    path('<int:item_id>/',views.details,name='details'),
    #add items
    path('add',views.create_item,name='create_item'),
    #exit
    path('update/<int:id>/',views.update_item,name='update_item'),
    path('delete/<int:id>/',views.delete_item,name='delete_item'),
]