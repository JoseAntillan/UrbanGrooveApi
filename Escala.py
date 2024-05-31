import random
import copy
import pretty_midi



class AcordesCmenor:
    Cm1 = ["C","C","D#","G"]
    Ddim2 = ["D","D","F","G#"]
    Dsos3 = ["D#","D#", "G", "A#"]
    Fm4 = ["F","F","G#","C"]
    Gm5 = ["G","G", "A#", "D"]
    Gsos6 = ["G#", "G#", "C", "D#"]
    Asos7 = ["A#","A#", "D", "F"]

    @staticmethod
    def DarTipoDeAcorde():
        # Definir al azar si el Acorde 1 será con Septima menor, 9 menor o normal
        Num = random.randint(1, 3)
        if Num == 1:
            # m7
            AcordesCmenor.Cm1 = ["C", "C", "D#", "G", "A#"]
        if Num == 2:
            # m9
            AcordesCmenor.Cm1 = ["C", "C", "D#", "G", "A#","D"]

        # Definir al azar si el Acorde 3 será con Septima mayor, 9 mayor o normal
        Num = random.randint(1, 3)
        if Num == 1:
            # M7
            AcordesCmenor.Dsos3 = ["D#", "D#", "G", "A#", "D"]
        if Num == 2:
            # M9
            AcordesCmenor.Dsos3 = ["D#", "D#", "G", "A#", "D","F"]

        # Definir al azar si el Acorde 4 será con Septima menor, 9 menor o normal
        Num = random.randint(1, 3)
        if Num == 1:
            # m7
            AcordesCmenor.Fm4 = ["F", "F", "G#", "C", "D#"]
        if Num == 2:
            # m9
            AcordesCmenor.Fm4 = ["F", "F", "G#", "C", "D#","G"]

        # Definir al azar si el Acorde 5 será con Septima menor, 9 menor o normal
        Num = random.randint(1, 3)
        if Num == 1:
            #m7
            AcordesCmenor.Gm5 = ["G", "G", "A#", "D", "F"]
        if Num == 2:
            #m9
            AcordesCmenor.Gm5 = ["G", "G", "A#", "D", "F","A"]
        if Num == 3:
            #Modo harmonico, en vez de la nota A# se sube 1 semitono hacia B
            # MINOR HARMONIC
            AcordesCmenor.Gm5 = ["G", "G", "B", "D", "F"]



        # Definir al azar si el Acorde 6 será con Septima mayor, 9 mayor o normal
        Num = random.randint(1, 3)
        if Num == 1:
            # M7
            AcordesCmenor.Gsos6 = ["G#", "G#", "C", "D#","G"]
        if Num == 2:
            # M9
            AcordesCmenor.Gsos6 = ["G#", "G#", "C", "D#","G","A#"]

        # Definir al azar si el Acorde 7 será con Septima mayor, 9 mayor o normal
        Num = random.randint(1, 3)
        if Num == 1:
            # M7

             AcordesCmenor.Asos7 = ["A#","A#", "D", "F","A"]
        if Num == 2:
            # M9
            AcordesCmenor.Asos7 = ["A#","A#", "D", "F","A","C"]

    def ObtenerAcordeConNum(numero):



        global acorde
        if numero == 1:
            acorde = AcordesCmenor.Cm1

        if numero == 2:
            acorde = AcordesCmenor.Ddim2

        if numero == 3:
            acorde = AcordesCmenor.Dsos3

        if numero == 4:
            acorde = AcordesCmenor.Fm4

        if numero == 5:
            acorde = AcordesCmenor.Gm5

        if numero == 6:
            acorde = AcordesCmenor.Gsos6

        if numero == 7:
            acorde = AcordesCmenor.Asos7

        return acorde

    @staticmethod
    #con la variable PrimerAcorde podemos iniciar la progresion desde el grado que queramos (1,2,3,4,5,6,7)
    #si el valor de PrimerAcorde es 0, el valor del primer grado será random
    def CrearProgresion(PrimerAcorde):
        chords = []
        progresion = []

        if PrimerAcorde == 0:
            PrimerAcorde = random.randint(1, 7)
        chords.append(copy.deepcopy(AcordesCmenor.ObtenerAcordeConNum(PrimerAcorde)))
        Next = AcordesCmenor.nextChord(PrimerAcorde)
        progresion.append(copy.deepcopy(PrimerAcorde))

        for x in range(0,3):


            progresion.append(copy.deepcopy(Next))


            chords.append(copy.deepcopy(AcordesCmenor.ObtenerAcordeConNum(Next)))
            Next = AcordesCmenor.nextChord(Next)

        for x in range(0, len(progresion)):
            if progresion[x] == 1:
                progresion[x] = "I"
            elif progresion[x] == 2:
                progresion[x] = "II"
            elif progresion[x] == 3:
                progresion[x] = "III"
            elif progresion[x] == 4:
                progresion[x] = "IV"
            elif progresion[x] == 5:
                progresion[x] = "V"
            elif progresion[x] == 6:
                progresion[x] = "VI"
            else:
                progresion[x] = "VII"




        chords, progresion = AcordesCmenor.ConcTipo(chords,progresion)

        return chords,progresion


    def ConcTipo(chords, progresion):
        #recorrer la lista de numeros de la progresion para
        #agregar si el acorde es Mayor, menor, Disminuido o bM7


        #x recorre la progresion con numeros
        for x in range(0, len(progresion)):
            contieneB = False
            if progresion[x] == "I" or progresion[x] == "IV" or progresion[x] == "V":
                #el acorde 5 es el unico que puede ser b-7
                if progresion[x] == "V":
                    #con z recorremos cada elemento de los acordes para averiguar si contiene la letra B
                    #si es asi significa que el acorde es b-7 por lo que le agregaremos la letra b antes

                    for z in range(0,len(chords[x])):
                        if chords[x][z] == "B":
                            contieneB = True
                    if contieneB:
                        progresion[x] = "b"+str(progresion[x])
                    else:
                        progresion[x] = str(progresion[x]) + "m"

                else:
                    progresion[x] = str(progresion[x]) + "m"

            elif progresion[x] == "III" or progresion[x] == "VI" or progresion[x] == "VII":
                progresion[x] = str(progresion[x]) + "M"
            else:
                progresion[x] = str(progresion[x]) + "dim"
        for x in range(0, len(chords)):
            if len(chords[x]) == 6:
                progresion[x] = str(progresion[x]) + "9"
            elif len(chords[x]) == 5:
                progresion[x] = str(progresion[x]) + "7"

        return chords, progresion


    def nextChord(numero):
        N = random.randint(1, 100)
        ProbabilidadUsual = 65
        ProbabilidadCasual = 25
        ProbabilidadRara = 10

        # si el acorde de entrada es el numero 1:
        if numero == 1:
            # el valor es menor que la probabilidad usual ?
            if N <= ProbabilidadUsual:
                Next = random.randint(1, 2)
                if Next == 1:
                    return 4
                else:
                    return 5
                # el valor es > que la probabilidad usual? y tambien es <= ProbabilidadUsual+ProbabilidadCasual?(osea que es probabilidad rara)

            elif N > ProbabilidadUsual and N <= ProbabilidadUsual + ProbabilidadCasual:
                return 6
            else:
                Next = random.randint(1, 2)
                if Next == 1:
                    return 2
                else:
                    return 3

            # si el acorde de entrada es el numero 2:
        if numero == 2:
            # el valor es menor que la probabilidad usual ?
            if N <= ProbabilidadUsual:
                return 5
            # el valor es > que la probabilidad usual? y tambien es <= ProbabilidadUsual+ProbabilidadCasual?
            elif N > ProbabilidadUsual and N <= ProbabilidadUsual + ProbabilidadCasual:
                Next = random.randint(1, 2)
                if Next == 1:
                    return 4
                else:
                    return 6
            else:
                Next = random.randint(1, 2)
                if Next == 1:
                    return 1
                else:
                    return 3

        # si el acorde de entrada es el numero 3:
        if numero == 3:
            # el valor es menor que la probabilidad usual ?
            if N <= ProbabilidadUsual:
                return 6
            # el valor es > que la probabilidad usual? y tambien es <= ProbabilidadUsual+ProbabilidadCasual?
            elif N > ProbabilidadUsual and N <= ProbabilidadUsual + ProbabilidadCasual:
                return 4
            else:
                Next = random.randint(1, 3)
                if Next == 1:
                    return 1
                elif Next == 2:
                    return 2
                else:
                    return 5

            # si el acorde de entrada es el numero 4:
        if numero == 4:
            # el valor es menor que la probabilidad usual ?
            if N <= ProbabilidadUsual:
                return 5
            # el valor es > que la probabilidad usual? y tambien es <= ProbabilidadUsual+ProbabilidadCasual?
            elif N > ProbabilidadUsual and N <= ProbabilidadUsual + ProbabilidadCasual:
                Next = random.randint(1, 2)
                if Next == 1:
                    return 1
                else:
                    return 2
            else:
                Next = random.randint(1, 2)
                if Next == 1:
                    return 3
                else:
                    return 6
        # si el acorde de entrada es el numero 5:
        if numero == 5:
            # el valor es menor que la probabilidad usual ?
            if N <= ProbabilidadUsual:
                return 1
            # el valor es > que la probabilidad usual? y tambien es <= ProbabilidadUsual+ProbabilidadCasual?
            elif N > ProbabilidadUsual and N <= ProbabilidadUsual + ProbabilidadCasual:
                Next = random.randint(1, 2)
                if Next == 1:
                    return 4
                else:
                    return 6
            else:
                Next = random.randint(1, 2)
                if Next == 1:
                    return 2
                else:
                    return 3
        # si el acorde de entrada es el numero 6
        if numero == 6:
            # el valor es menor que la probabilidad usual ?
            if N <= ProbabilidadUsual:
                Next = random.randint(1, 2)
                if Next == 1:
                    return 2
                else:
                    return 5
                # el valor es > que la probabilidad usual? y tambien es <= ProbabilidadUsual+ProbabilidadCasual?
            elif N > ProbabilidadUsual and N <= ProbabilidadUsual + ProbabilidadCasual:
                Next = random.randint(1, 2)
                if Next == 1:
                    return 3
                else:
                    return 4
            else:
                return 1

        # si el acorde de entrada es el numero 7
        if numero == 7:
            # el valor es menor que la probabilidad usual ?
            if N <= ProbabilidadUsual:
                Next = random.randint(1, 2)
                if Next == 1:
                    return 1
                else:
                    return 3
                # el valor es > que la probabilidad usual? y tambien es <= ProbabilidadUsual+ProbabilidadCasual?
            elif N > ProbabilidadUsual and N <= ProbabilidadUsual + ProbabilidadCasual:
                return 6
            else:
                Next = random.randint(1, 3)
                if Next == 1:
                    return 2
                elif Next == 2:
                    return 4
                else:
                    return 5

def CrearMidi(Acordes):
    Ac = Acordes.copy()

    for x in range (0,len(Ac)):
        for z in range (0,len(Ac[x])):
            note_number = pretty_midi.note_name_to_number(Ac[x][z]) - 12
            Ac[x][z] = note_number
    return Ac


def DarEscala(Progresion):
    for acorde in range(0, len(Progresion)):
        for nota in range(0, len(Progresion[acorde])):
            if nota == 0:
                NotaActual = Progresion[acorde][nota]
                if NotaActual == "G" or NotaActual == "G#" or NotaActual == "A" or NotaActual == "A#" or NotaActual == "B":
                    Progresion[acorde][nota] += "3"
                else:
                    Progresion[acorde][nota] += "4"

            else:
                Progresion[acorde][nota] += "5"

    return Progresion






