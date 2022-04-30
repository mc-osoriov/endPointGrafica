from django.shortcuts import render
import sqlite3

# Create your views here.
def index(request):

    dataBase = sqlite3.connect("db.sqlite3")
    curr = dataBase.cursor()
    query = '''SELECT NumNivel, Duracion FROM Juego WHERE IdUsuario = 1234'''
    rows = curr.execute(query)
    data = [['Nivel', 'Tiempo']]
    for x in rows:
        data.append([ x[0], x[1]])

    #print(data)

    return render(request, 'graficaApp/index.html', {'valores': data})

