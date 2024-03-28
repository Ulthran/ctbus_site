import memcache
import os
import spotipy

from dotenv import load_dotenv
from flask import (
    Flask,
    redirect,
    render_template,
    request,
    send_from_directory,
    session,
)
from flask_sitemapper import Sitemapper

# from flask_session import Session

from app import project_pages, random_third_attribute
from app.data_utils import get_chess_stats

load_dotenv()

sitemapper = Sitemapper()
app = Flask(__name__)
app.secret_key = os.urandom(12)
sitemapper.init_app(app)

# if os.environ.get("FLASK_DEBUG", 0):
#    app.config["SESSION_TYPE"] = "filesystem"
#    app.config["SESSION_FILE_DIR"] = "./.flask_session/"
# else:
#    app.config["SESSION_TYPE"] = "memcached"
#    app.config["SESSION_MEMCACHED"] = memcache.Client(
#        ["ctbus-site-cache-tncxie.serverless.use1.cache.amazonaws.com:11211"]
#    )
#    app.config["SESSION_PERMANENT"] = False

# Session(app)

CDN_URL = os.environ.get("CDN_URL", "")


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
    return render_template(
        "index.html",
        cdn_url=CDN_URL,
        third_attr=random_third_attribute(),
    )


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", cdn_url=CDN_URL), 404


@sitemapper.include(
    lastmod="2023-11-29",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/pcmp")
def pcmp():
    return render_template("pcmp.html", cdn_url=CDN_URL)


@sitemapper.include(
    lastmod="2023-11-29",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/music")
def music():
    print("START")
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    print(session)
    print(cache_handler.get_cached_token())
    print("AUTH")
    auth_manager = spotipy.oauth2.SpotifyOAuth(
        scope="user-read-currently-playing",
        cache_handler=cache_handler,
        show_dialog=True,
    )
    print(session)
    print(cache_handler.get_cached_token())
    print(auth_manager.validate_token(cache_handler.get_cached_token()))

    if request.args.get("code"):
        # Step 2. Being redirected from Spotify auth page
        auth_manager.get_access_token(request.args.get("code"))
        return redirect("/music")

    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        # Step 1. Display sign in link when no token
        auth_url = auth_manager.get_authorize_url()
        print(auth_url)
        return render_template("music.html", cdn_url=CDN_URL, auth_url=auth_url)

    # Step 3. Signed in, display data
    spotify = spotipy.Spotify(auth_manager=auth_manager)
    return render_template(
        "music.html", cdn_url=CDN_URL, playlists=spotify.current_user_playlists()
    )


@sitemapper.include(
    lastmod="2023-11-29",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/projects")
def projects():
    return render_template("projects.html", cdn_url=CDN_URL)


@sitemapper.include(url_variables={"project": project_pages()})
@app.route("/projects/<project>")
def project(project):
    return render_template(f"projects/{project}.html", cdn_url=CDN_URL)


@sitemapper.include(
    lastmod="2023-11-29",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/sports")
def sports():
    return render_template(
        "sports.html", cdn_url=CDN_URL, chess_stats=get_chess_stats()
    )


@sitemapper.include(
    lastmod="2023-11-29",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/certifications")
def certifications():
    return render_template("certifications.html", cdn_url=CDN_URL)


@sitemapper.include(
    lastmod="2023-11-29",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/favorite-number")
def favorite_number():
    return render_template("favorite-number.html", cdn_url=CDN_URL)


@sitemapper.include(
    lastmod="2023-11-29",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/session")
def session_info():
    session["test"] = "test"
    return render_template("session.html", cdn_url=CDN_URL, session=session)


@app.route("/remove-session-data/<key>")
def remove_session_data(key):
    session.pop(key, None)
    return redirect("/session")


@app.route("/sitemap.xml")
def r_sitemap():
    return sitemapper.generate()


@app.after_request
def add_security_headers(resp):
    resp.headers["Content-Security-Policy"] = "default-src 'self'"
    resp.headers["Content-Security-Policy"] = "style-src 'self' cdn.jsdelivr.net/npm/"
    resp.headers["Content-Security-Policy"] = (
        "script-src 'self' cdn.jsdelivr.net/npm/ cdnjs.cloudflare.com/ajax polyfill.io"
    )

    resp.headers["Content-Security-Policy"] = "frame-ancestors 'none'"
    return resp


if __name__ == "__main__":
    app.run()
