from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
import speech_recognition as sr

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)

    return render_template('index.html', transcript=transcript)


@app.route("/documento_sad",  methods=["GET"])
def vista_sad():
    return render_template('documento_sad.html')


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
