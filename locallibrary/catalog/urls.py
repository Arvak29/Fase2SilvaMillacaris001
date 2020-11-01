from django.urls import path
from . import views
from django.conf.urls import url
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('Store/<int:pk>',views.PlataformGameView.as_view(),name='Store'),
    path ('user/<int:pk>', views.UserDetailView.as_view(), name='user_detail'),
]

urlpatterns+=[
    path('user/create/', views.UserCreate.as_view(), name='user_create'),
    path('user/<int:pk>/update/', views.UserUpdate.as_view(), name='user_update'),
    path('user/<int:pk>/delete/', views.UserDelete.as_view(success_url="/"), name='user_delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)