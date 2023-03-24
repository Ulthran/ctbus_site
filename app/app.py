import os
from flask import Flask, render_template, url_for, request, redirect, flash, send_from_directory
from DynamoDB import DynamoDB

app = Flask(__name__)
app.secret_key = os.urandom(12)

#bucket = os.environ.get('BUCKET', 'ctbus-site-db')
table_name = os.environ.get('TABLE', 'ctbus-site-db')
db = DynamoDB(table_name)

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
  return render_template('projects.html', project_dict=db.projects_dict())

@app.route('/project/<project_name>')
def project(project_name):
  return render_template('project.html', project_dict=db.project_dict(project_name))

if __name__ == "__main__":
  app.run(debug=True)
