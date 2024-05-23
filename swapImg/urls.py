from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.avatarView, name='user-info'),
    path('success/', views.uploadok, name = 'success'),
    path('listing/', views.DisplayRegisteredUser, name = 'user-info-listing'),
    # path('process-image/', views.anime_face_generator, name='anime_face_generator'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
