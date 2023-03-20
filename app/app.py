import os
from flask import Flask, render_template, url_for, request, redirect, flash, send_from_directory
from lib import S3

app = Flask(__name__)
app.secret_key = os.urandom(12)

bucket = os.environ.get('BUCKET')
db = S3.S3(bucket)

@app.route('/favicon.ico')
def favicon():
  return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/resume')
def resume():
  return render_template('resume.html')

@app.route('/projects')
def projects():
  return render_template('projects.html', project_list=db.list_projects())

@app.route('/project/<project_name>')
def project(project_name):
  return render_template('project.html', project_name=project_name)

if __name__ == "__main__":
  app.run(debug=True)
