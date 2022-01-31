from rest_framework import serializers

from apps.morse_app.models import Morse

class MorseSerializer(serializers.ModelSerializer):
    completo  =serializers.SerializerMethodField('get_completo')
    class Meta:
        model = Morse
        fields = (
            'id',
            'codigo',
            'caracter',
            'completo',
        )
    
    def get_completo(self, instance):
        return f"{instance.id} {instance.caracter} {instance.codigo}"