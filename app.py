from flask import Flask, request, redirect, url_for, render_template, flash


app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
def home():
    return render_template('index.html')