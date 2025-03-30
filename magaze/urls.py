# Конфигурация URL для проекта magaze.

# Список `urlpatterns` направляет URL-адреса на представления.  
# Для получения дополнительной информации см.:
#     https://docs.djangoproject.com/en/5.1/topics/http/urls/

# Примеры:  
# Функции-представления:
#     1. Добавьте импорт: `from my_app import views`
#     2. Добавьте URL в urlpatterns: `path('', views.home, name='home')`

# Классы-представления:
#     1. Добавьте импорт: `from other_app.views import Home`
#     2. Добавьте URL в urlpatterns: `path('', Home.as_view(), name='home')`

# Добавление другой конфигурации URL:
#     1. Импортируйте функцию `include`: `from django.urls import include, path`
#     2. Добавьте URL в urlpatterns: `path('blog/', include('blog.urls'))`

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('', include('cart.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)