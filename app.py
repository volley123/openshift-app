import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask python application running on openshift cluster'
    
@app.route('/how are you')
def hello():
     return 'I am good, how about you?'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
