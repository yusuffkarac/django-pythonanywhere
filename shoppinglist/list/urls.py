from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.index, name='index'),
    path('bought', views.bought, name='bought'),

    path('add_product/', views.add_product, name='add_product'),
    path('delete_item/<int:id>', views.delete_item, name='delete_item'),
    path('delete_bought_item/<int:id>', views.delete_bought_item, name='delete_bought_item'),
    path('bought_item/<int:id>', views.bought_item, name='bought_item'),

] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)