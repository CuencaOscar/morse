from apps.morse_app.respositories import MorseRepository


class BinaryToMorse():

    def transform(self, text):
        list_one = []
        list_zero = []
        count_one = 0
        count_zero = 0
        for i, number in enumerate(text):
            if (number == "1"):
                count_one = count_one + 1
                if(count_zero != 0):
                    if(count_zero not in list_zero):
                        list_zero.append(count_zero)
                    count_zero = 0
                if(i == len(text)-1):
                    list_one.append(count_one)
            else:
                count_zero = count_zero + 1
                if (count_one != 0):
                    if(count_one not in list_one):
                        list_one.append(count_one)
                    count_one = 0
        list_one.sort()
        list_zero.sort()

        initial_one = list_one[0]
        dot = [initial_one]  # Rango permitido para tipear un punto
        initial_zero = list_zero[0]
        # Rango permitido para tipear una pausa mientras se esta formando una letra
        pause = [initial_zero]

        for _ in list_one:
            if (_+1 in list_one):
                dot.append(_+1)
            else:
                break

        for _ in list_zero:
            if (_+1 in list_zero):
                pause.append(_+1)
            else:
                break
        line = list_one[len(dot):]  # Rango permitido para tipear un guion
        # Rango permitido para dar espacio luego de finalizar una palabra
        nextLetter = list_zero[len(pause):len(list_zero)-1]
        nextWord = [list_zero[-1]]

        count_one = 0
        count_zero = 0
        list_words = []
        for _ in text:
            if (_ == "1"):
                count_one = count_one + 1
                if(count_zero in pause):
                    count_zero = 0
                elif(count_zero in nextLetter):
                    list_words.append(" ")
                    count_zero = 0
                elif(count_zero in nextWord):
                    list_words.append("   ")
                    count_zero = 0
            else:
                count_zero = count_zero + 1
                if(count_one in dot):
                    list_words.append(".")
                    count_one = 0
                elif(count_one in line):
                    list_words.append("-")
                    count_one = 0

        return " ".join("".join(list_words[1:]).split(" "))
   
    def traslate_to_human(self, text):
        palabras = text.split("   ")
        resp = ""
        for palabra in palabras:
            letras = palabra.split(" ")
            print(letras)
            for letra in letras:
                change = MorseRepository().get_char_by_codigo(letra)
                resp += change[0].caracter if change else letra
            resp += " "
        resp = resp[:-1] if resp else resp
        return resp

    def traslate_to_morse(self, text):
        resp = ""
        for i in text:
            print(i)
            change = MorseRepository().get_codigo_by_char(i)
            resp += change[0].codigo + " " if change else i + " "
        resp = resp[:-1] if resp else resp
        return resp