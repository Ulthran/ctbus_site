import os
from flask import Flask, render_template, send_from_directory
from app.DynamoDB import DynamoDB
from app.S3 import S3

app = Flask(__name__)
app.secret_key = os.urandom(12)

bucket = os.environ.get('BUCKET', 'ctbus-site-db')
s3 = S3(bucket)
ENV = s3.get_env()
table_name = os.environ.get("TABLE", "ctbus-site-db")
db = DynamoDB(table_name)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@app.route("/")
def index():
    return render_template("index.html", cdn_url=ENV.get("CDN_URL", ""))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', cdn_url=ENV.get("CDN_URL", "")), 404


@app.route("/resume")
def resume():
    return render_template("resume.html", cdn_url=ENV.get("CDN_URL", ""))


@app.route("/pcmp")
def pcmp():
    return render_template("pcmp.html", cdn_url=ENV.get("CDN_URL", ""))


@app.route("/music")
def music():
    return render_template("music.html", cdn_url=ENV.get("CDN_URL", ""))


@app.route("/physics")
def physics():
    return render_template("physics.html", cdn_url=ENV.get("CDN_URL", ""))


@app.route("/projects")
def projects():
    return render_template("projects.html", cdn_url=ENV.get("CDN_URL", ""), project_dict=db.projects_dict())


@app.route("/project/<project_name>")
def project(project_name):
    return render_template("project.html", cdn_url=ENV.get("CDN_URL", ""), project_dict=db.project_dict(project_name))


if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
