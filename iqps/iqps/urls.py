from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('frontend.urls')),
    path('request/', include('request.urls')),
    path('admin/', admin.site.urls),
    path('data/', include('data.urls')),
    path('upload/', include('upload.urls')),
    path('accounts/', include('accounts.urls')),
    path('search/', include('search.urls')),
    path('select2/', include('django_select2.urls')),
    path('captcha/', include('captcha.urls'))
]
