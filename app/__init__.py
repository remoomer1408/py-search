from flask import Flask

app = Flask(__name__)
app.config.from_object('config') #Load configurations

from app import routes  #Import routes after initialising the app. 