from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contacto", methods=["POST"])
def contacto():
    nombre = request.form["nombre"]
    email = request.form["email"]
    mensaje = request.form["mensaje"]
    print(f"Mensaje de {nombre} ({email}): {mensaje}")
    return "¡Gracias por contactarte! Te responderemos pronto."

if __name__ == "__main__":
    app.run(debug=True)
