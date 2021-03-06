import os
from dotenv import load_dotenv

project_folder = os.path.expanduser('~/my-project-dir')  
load_dotenv(os.path.join(project_folder, '.env'))

from flask import Flask, render_template
import main

app = Flask(__name__)

@app.route("/")
def ready():
    print("bot is ready")
    ##main code file##
    crypto = main()
    return render_template('index.html') 
    crypto.run()  

if (__name__ == "__main__"):
    app.run()
    
