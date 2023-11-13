import os
from flask import Flask, render_template, send_from_directory
from app.data_utils import get_chess_stats
from app.S3 import S3

app = Flask(__name__)
app.secret_key = os.urandom(12)

bucket = os.environ.get("BUCKET", "ctbus-site-db")
s3 = S3(bucket)
ENV = s3.get_env()


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
    return render_template("error.html", cdn_url=ENV.get("CDN_URL", "")), 404


@app.route("/pcmp")
def pcmp():
    return render_template("pcmp.html", cdn_url=ENV.get("CDN_URL", ""))


@app.route("/music")
def music():
    return render_template("music.html", cdn_url=ENV.get("CDN_URL", ""))


@app.route("/projects")
def projects():
    return render_template("projects.html", cdn_url=ENV.get("CDN_URL", ""))


@app.route("/projects/<project>")
def project(project):
    return render_template(f"projects/{project}.html", cdn_url=ENV.get("CDN_URL", ""))


@app.route("/sports")
def sports():
    return render_template(
        "sports.html", cdn_url=ENV.get("CDN_URL", ""), chess_stats=get_chess_stats()
    )


@app.route("/certifications")
def certifications():
    return render_template("certifications.html", cdn_url=ENV.get("CDN_URL", ""))


@app.route("/favorite-number")
def favorite_number():
    return render_template("favorite-number.html", cdn_url=ENV.get("CDN_URL", ""))


if __name__ == "__main__":
    app.run()
