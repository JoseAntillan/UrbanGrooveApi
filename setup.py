import copy
import random
from flask_cors import CORS
from pretty_midi import pretty_midi
from Escala import AcordesCmenor
import Escala
from Escala import DarEscala
from flask import Flask, render_template
from flask import jsonify, request

def create_app(enviroment):
    app = Flask(__name__)
    app.config.from_object(enviroment)



    return app

def CrearProgresionJson(Transponer, GradoInicial):
    #Definir si los acordes de cada numero seran Maj9,Maj7, min9  o min7
    AcordesCmenor.DarTipoDeAcorde()

    #generar la progresion, y los grados en numeros
    #el valor que enviamos es el grado por el que queremos comenzar la progresion
    Progresion, ProgresionNumbers = Escala.AcordesCmenor.CrearProgresion(int(GradoInicial))

    #Dar escala a las notas individuales de los acordes, EJ: C -> C5
    Progresion = DarEscala(Progresion)


    if int(Transponer) == 0:
        Transponer = random.randint(-6,6)
    elif int(Transponer) > 0:
        Transponer = int(Transponer) -1


    Ac = copy.deepcopy(Progresion)
    for x in range(0, len(Ac)):
        for z in range(0, len(Ac[x])):
            note_number = pretty_midi.note_name_to_number(Ac[x][z])
            Ac[x][z] = note_number + int(Transponer)


    Ac2 = copy.deepcopy(Ac)
    for x in range(0, len(Ac2)):
        for z in range(0, len(Ac2[x])):
            note_name = pretty_midi.note_number_to_name(Ac2[x][z])
            Ac2[x][z] = note_name


    root = int(Transponer)

    if root == -6:
        root = "F#"
    elif root == -5:
        root ="G"
    elif root == -4:
        root ="G#"
    elif root == -3:
        root ="A"
    elif root == -2:
        root ="A#"
    elif root == -1:
        root ="B"
    elif root == 1:
        root ="C#"
    elif root == 2:
        root ="D"
    elif root == 3:
        root ="D#"
    elif root == 4:
        root ="E"
    elif root == 5:
        root ="F"
    else:
        root ="C"

    ObjetoJson = {'Acordes':Ac2, 'Grados': ProgresionNumbers, 'Numeros': Ac, 'Root':root }
    return ObjetoJson


app = Flask(__name__)
CORS(app)

#enviroment = config['development']
#if config_decouple('PRODUCTION', default=False):
 #  enviroment = config['production']

#app = create_app(enviroment)



@app.route("/api/v1/<transponer>/<int:gradoinicial>")
@app.route("/api/v1/<transponer>")
@app.route("/api/v1")
@app.route("/api")
def action(transponer = 0, gradoinicial = 1):
    return jsonify(CrearProgresionJson(transponer,gradoinicial))

@app.route("/")
def index():
    return render_template("index.html")




if __name__ == '__main__':
    app.run()
