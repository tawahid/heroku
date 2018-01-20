from django.urls import path, include
from core.views import offeringView,studioView, error_404, error_500
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', offeringView, name='offeringView'),
    path('studio', studioView, name='studioView'),
]

handler404 = error_404
handler500 = error_500