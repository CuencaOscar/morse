from .models import Morse


class MorseRepository():

    def getCodigos(self):
        return Morse.objects.all()

    def get_codigo_by_char(self, character):
        return Morse.objects.filter(caracter=character).all()

    def get_char_by_codigo(self, codigo):
        return Morse.objects.filter(codigo=codigo).all()

