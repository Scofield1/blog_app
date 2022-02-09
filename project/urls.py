from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit-blog/<str:pk>', views.edit_blog, name='edit_blog'),
    path('delete-blog/<str:pk>', views.delete_blog, name='delete_blog'),
    path('blog-details/<str:pk>', views.blog_details, name='blog_details'),
    path('create-blog', views.create_blog, name='create_blog'),

    path('register/', views.register, name='register'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
