from django.urls import path

from .views import(
    subscription,subscription_view,
)

app_name='subs'
urlpatterns = [
    path('subscribe/',subscription,name='subscribe'),
    path('make-payment-subscribe/',subscription_view,name='make-payment-subscribe'),

]