"""Membuat Base WEB"""
from flask import Flask,render_template

app  = Flask (__name__)

@app.route ('/')
def home():
    """Menampilkan Halaman Home"""
    return render_template ('home.html')

@app.route ('/About')
def about ():
    """Menampilkan Halaman About"""
    return render_template ('about.html')

if __name__ == ('__main__'):
    app.run (debug=True)
