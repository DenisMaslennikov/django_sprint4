from typing import List

from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include, URLPattern
from django.conf import settings


handler403 = 'pages.views.permission_denied'
handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'

urlpatterns: List[URLPattern] = [
    path('pages/', include('pages.urls', namespace='pages')),
    path('', include('users.urls', namespace='users')),
    path('', include('blog.urls', namespace='blog')),
    # Вся логика работы с пользователями в приложении users.
    # Но pytest требовал добавленного в явном виде инклуда в этот urls.
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
