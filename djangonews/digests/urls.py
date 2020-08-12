from django.urls import path, include

from . import views




urlpatterns = [
    #path('profile', views.profile, name="accounts_my_profile"),
    path('subscribe', views.subscribe, name="digests_subscribe"),
    path('subscriptions', views.my_subscriptions, name="digests_subscriptions"),

    path('unsubscribe', views.unsubscribe, name='digests_unsubscribe'),
    path('unsubscribe/<uuid:subscription_id>/<uuid:digests_id>', views.unsubscribe, name='digests_unsubscribe'),

]
