from django.urls import path
from . import views
# This allow you to display images from your static 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.mainpage,name='mainpage'), 
    path("info", views.information,name='info'),
    path("update <str:pk>", views.update,name='update'),
    path("delete <str:pk>", views.delete,name='delete'),
]
# This allow you to display images from your static 
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)