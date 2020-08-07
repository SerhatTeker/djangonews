from django.urls import path, include

from . import views




urlpatterns = [
    #path('profile', views.profile, name="accounts_my_profile"),
    path('subscribe', views.subscribe, name="digest_subscribe"),
    path('subscriptions', views.my_subscriptions, name="digest_subscriptions"),

    path('unsubscribe', views.unsubscribe, name='digest_unsubscribe'),
    path('unsubscribe/<uuid:subscription_id>/<uuid:digest_id>', views.unsubscribe, name='digest_unsubscribe'),

]
