from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('lomake.html')

@app.route("/vastaus")
def vastaus():
    
    uusi_nimi = request.args['nimi']
    uusi_nimi = uusi_nimi[::-1]
    return render_template('vastaus.html', uusi_nimi=uusi_nimi)

if __name__ == '__main__':
    app.run()
