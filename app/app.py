import os
from flask import Flask, make_response, render_template, send_from_directory
from flask_sitemapper import Sitemapper
from app import project_pages
from app.data_utils import get_chess_stats

sitemapper = Sitemapper()
app = Flask(__name__)
app.secret_key = os.urandom(12)
sitemapper.init_app(app)
ENV = {"CDN_URL": "https://d2w4s6xs8769uj.cloudfront.net"}


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@sitemapper.include(
    lastmod="2023-11-29",
    changefreq="monthly",
    priority=1.0,
)
@app.route("/")
def index():
    return render_template("index.html", cdn_url=ENV.get("CDN_URL", ""))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", cdn_url=ENV.get("CDN_URL", "")), 404


@sitemapper.include(
    lastmod="2023-11-29",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/pcmp")
def pcmp():
    return render_template("pcmp.html", cdn_url=ENV.get("CDN_URL", ""))


@sitemapper.include(
    lastmod="2023-11-29",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/music")
def music():
    return render_template("music.html", cdn_url=ENV.get("CDN_URL", ""))


@sitemapper.include(
    lastmod="2023-11-29",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/projects")
def projects():
    return render_template("projects.html", cdn_url=ENV.get("CDN_URL", ""))


@sitemapper.include(url_variables={"project": project_pages()})
@app.route("/projects/<project>")
def project(project):
    return render_template(f"projects/{project}.html", cdn_url=ENV.get("CDN_URL", ""))


@sitemapper.include(
    lastmod="2023-11-29",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/sports")
def sports():
    return render_template(
        "sports.html", cdn_url=ENV.get("CDN_URL", ""), chess_stats=get_chess_stats()
    )


@sitemapper.include(
    lastmod="2023-11-29",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/certifications")
def certifications():
    return render_template("certifications.html", cdn_url=ENV.get("CDN_URL", ""))


@sitemapper.include(
    lastmod="2023-11-29",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/favorite-number")
def favorite_number():
    return render_template("favorite-number.html", cdn_url=ENV.get("CDN_URL", ""))


@app.route("/sitemap.xml")
def r_sitemap():
    return sitemapper.generate()


@app.after_request
def add_security_headers(resp):
    resp.headers["Content-Security-Policy"] = "default-src 'self'"
    resp.headers["Content-Security-Policy"] = "style-src 'self' cdn.jsdelivr.net/npm/"
    resp.headers[
        "Content-Security-Policy"
    ] = "script-src 'self' cdn.jsdelivr.net/npm/ cdnjs.cloudflare.com/ajax polyfill.io"

    resp.headers["Content-Security-Policy"] = "frame-ancestors 'none'"
    return resp


if __name__ == "__main__":
    app.run()
