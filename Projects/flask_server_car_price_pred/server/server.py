from flask import Flask, jsonify, request
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)