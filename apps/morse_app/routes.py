from django.urls import path
from apps.morse_app.views import MorseViewSet

urlpatterns = [
    path('', MorseViewSet.as_view({'get': 'list','post': 'create'}), name='morse_list'),
    path('traslate_to_morse', MorseViewSet.as_view({'post': 'traslate_to_morse'}), name='traslate_to_morse'),
    path('traslate_to_human', MorseViewSet.as_view({'post': 'traslate_to_human'}), name='traslate_to_human'),
    path('decode_bits_to_morse', MorseViewSet.as_view({'post': 'decode_bits_to_morse'}), name='decode_bits_to_morse'),
]