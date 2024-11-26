app = Microdot()

# Definimos la ruta raíz
@app.route('/')
async def index(request):
    return send_file('index.html')




@app.route('/<dir>/<file>')
async def static(request, dir, file):
    return send_file("/{}/{}".format(dir, file))


@app.route('/toggle/led/<int:id>') # Definimos la ruta con un parámetro entero
async def index(request, id):

    # Dependiendo del valor del parámetro id, encendemos o apagamos un LED
    if id == 1:
        LED1.value(not LED1.value())

    elif id == 2:
        LED2.value(not LED2.value())

    elif id == 3:
        LED3.value(not LED3.value())

    return 'OK'
app.run(port=80)