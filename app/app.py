from flask import Flask, render_template, redirect, request, url_for, session, g, jsonify
import os
import hashlib
import random
import string
import uuid
from flask_pymongo import PyMongo, pymongo
import pymongo
from pymongo import UpdateOne
from bson import ObjectId
from time import localtime


app = Flask(__name__, static_url_path='/static')
app.secret_key = "7hasdhfnbfcdshckjf9jdfjnkl"


@app.route('/')
def home():
    return render_template('adminConsole/home.html')


if __name__ == "__main__":
    app.run(debug=True)