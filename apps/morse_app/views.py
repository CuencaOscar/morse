from urllib import response
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from apps.morse_app.models import Morse
from apps.morse_app.respositories import MorseRepository
from .serializers import MorseSerializer
from utils.binary_to_morse import BinaryToMorse
# Create your views here.


class MorseViewSet(viewsets.ViewSet):

    def list(self, request):
        codigos = MorseRepository().getCodigos()
        serializer = MorseSerializer(codigos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        for item in data:
            serializer = MorseSerializer(data=item)
            if serializer.is_valid():
                mostrar = serializer.save()
                print(mostrar)
        return Response(True, status=status.HTTP_200_OK)

    def decode_bits_to_morse(self, request):
        binarios = request.data.get("text")
        resp = BinaryToMorse().transform(binarios)
        return Response({"response": resp}, status=status.HTTP_200_OK)

    def traslate_to_human(self, request):
        text = request.data.get("text")
        resp = BinaryToMorse().traslate_to_human(text)
        return Response({"response": resp}, status=status.HTTP_200_OK)

    def traslate_to_morse(self, request):
        text = request.data.get("text")
        resp = BinaryToMorse().traslate_to_morse(text)
        return Response({"response": resp}, status=status.HTTP_200_OK)
