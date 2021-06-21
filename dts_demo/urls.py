from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cost/', include('cost_resourcing.urls')),
    path('', include('auth0authorization.urls')),
]
