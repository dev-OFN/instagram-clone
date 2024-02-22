from django.urls import path 
from directs import views 


app_name='directs'

urlpatterns = [
    path('inbox/', views.inbox, name='message'),
    path('directs/<username>',views.Direct,name='directs'),
    path('send/',views.SendMessage,name='send-message'),
    path('new/',views.UserSearch,name='user-search'),
    path('new/<username>',views.NewMessage,name='new-message'),
]
