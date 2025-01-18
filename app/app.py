import os

from dotenv import load_dotenv
from flask import (
    Flask,
    redirect,
    render_template,
    request,
    send_from_directory,
    session,
    url_for,
)
from flask_sitemapper import Sitemapper

from app import project_pages, random_third_attribute
from app.blog import post_list, posts
from app.data_utils import (
    get_chess_stats,
    get_ctbus_monthly_playlists,
    get_spotify_data,
    get_spotify_user,
    get_spotipy_auth_manager,
    pcmp_repo_badges,
)

load_dotenv()

sitemapper = Sitemapper()
app = Flask(__name__)
app.secret_key = os.urandom(12)
sitemapper.init_app(app)

CDN_URL = os.environ.get("CDN_URL", "")


@app.context_processor
def inject_variables():
    return dict(cdn_url=CDN_URL, third_attr=random_third_attribute())


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
    )


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404


@sitemapper.include(
    lastmod="2024-06-25",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/past_work")
def past_work():
    return render_template("past_work.html")


@sitemapper.include(
    lastmod="2023-11-29",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/pcmp")
def pcmp():
    return render_template("pcmp.html")


@sitemapper.include(
    lastmod="2024-03-29",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/pcmp/dashboard")
def pcmp_dashboard():
    return render_template("pcmp_dashboard.html", repo_badges=pcmp_repo_badges())


@sitemapper.include(
    lastmod="2024-06-25",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/pcmp/more")
def pcmp_more():
    return render_template("pcmp_more.html")


@sitemapper.include(
    lastmod="2023-11-29",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/music")
def music():
    cache_handler, auth_manager = get_spotipy_auth_manager(
        session, url_for("music", _external=True)
    )

    if request.args.get("code"):
        # Step 2. Being redirected from Spotify auth page
        auth_manager.get_access_token(request.args.get("code"))
        return redirect(url_for("music"))

    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        # Step 1. Display sign in link when no token
        auth_url = auth_manager.get_authorize_url()
        return render_template(
            "music.html",
            auth_url=auth_url,
            monthlies=get_ctbus_monthly_playlists(),
        )

    # Step 3. Signed in, display data
    return render_template(
        "music.html",
        spotify_user=get_spotify_user(auth_manager),
        monthlies=get_ctbus_monthly_playlists(),
    )


@app.route("/spotify_data")
def spotify_data():
    _, auth_manager = get_spotipy_auth_manager(
        session, url_for("music", _external=True)
    )
    time_frame = request.args.get("time_frame", None)
    num_tracks = request.args.get("num_tracks", None)
    playlistsQ = bool(request.args.get("playlistsQ", False))
    playlist_name = request.args.get("playlist_name", None)
    return get_spotify_data(
        auth_manager,
        time_frame=time_frame,
        num_tracks=num_tracks,
        playlistsQ=playlistsQ,
        playlist_name=playlist_name,
    )


@sitemapper.include(url_variables={"post": [post_list]})
@app.route("/blog")
@app.route("/blog/<post>")
def blog(post=None):
    if post:
        post_info = posts.get(
            post,
            {
                "title": "Uh oh!",
                "subtitle": "We can't find the metadata for this post :(",
                "tags": ["embarrassment", "shame"],
                "date": "01/01/01",
                "mod_date": "01/01/01",
            },
        )
        return render_template(
            f"blog/{post}.html",
            title=post_info["title"],
            subtitle=post_info["subtitle"],
            date=post_info["date"],
            mod_date=post_info["mod_date"],
            tags=post_info["tags"],
            img_link=f"{CDN_URL}/images/blog/{post.replace('-', '_')}.png",
        )
    return render_template("blog.html", posts=posts)


@sitemapper.include(
    lastmod="2023-11-29",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/projects")
def projects():
    return render_template("projects.html")


@sitemapper.include(url_variables={"project": project_pages()})
@app.route("/projects/<project>")
def project(project):
    return render_template(f"projects/{project}.html")


@sitemapper.include(
    lastmod="2023-11-29",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/sports")
def sports():
    return render_template("sports.html", chess_stats=get_chess_stats())


@sitemapper.include(
    lastmod="2024-09-27",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/education")
def education():
    return render_template("education.html")


@sitemapper.include(
    lastmod="2023-11-29",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/certifications")
def certifications():
    return render_template("certifications.html")


@sitemapper.include(
    lastmod="2024-09-25",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/about")
def about():
    return render_template("about.html")


@sitemapper.include(
    lastmod="2024-09-13",
    changefreq="monthly",
    priority=0.95,
)
@app.route("/resume")
def resume():
    return redirect(f"{CDN_URL}/documents/resume.pdf")


@sitemapper.include(
    lastmod="2023-11-29",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/favorite-number")
def favorite_number():
    return render_template("favorite-number.html")


@sitemapper.include(
    lastmod="2023-11-29",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/session")
def session_info():
    return render_template("session.html", session=session)


@app.route("/remove-session-data/<key>")
def remove_session_data(key):
    session.pop(key, None)
    return redirect(url_for("session_info"))


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
