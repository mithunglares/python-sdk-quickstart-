import requests  #pip install requests
import os
#Set enviroment Variable
os.environ['AUTOWRAPT_BOOTSTRAP'] = 'autodynatrace'
import autodynatrace

print("imported AutoDynatrace")

from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

@app.route('/test', methods=['GET'])
def test():
   ploads = {'things':2,'total':25}
   r = requests.get('https://httpbin.org/get',params=ploads)
   print(r.text)
   print(r.url)
   return(r.text)



if __name__ == '__main__':
   app.run()