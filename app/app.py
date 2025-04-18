import os
from dotenv import load_dotenv
from flask import (
    Flask,
    redirect,
    render_template,
    send_from_directory,
    session,
    url_for,
)
from flask_sitemapper import Sitemapper
from app import random_third_attribute
from app.blog import post_list, posts
from app.data_utils import (
    get_chess_stats,
    get_ctbus_monthly_playlists,
    pcmp_repo_badges,
)
from app.projects import projects_dict, project_list

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
    lastmod="2025-01-24",
    changefreq="monthly",
    priority=1.0,
)
@app.route("/")
def index():
    return render_template(
        "index.html",
        header_post=posts[post_list[0]],
        header_post_key=post_list[0],
        header_img_link=f"{CDN_URL}/images/blog/{post_list[0].replace('-', '_')}.png",
    )


@app.errorhandler(404)
@app.errorhandler(500)
def page_not_found(e):
    if e.code == 404:
        return (
            render_template(
                "error.html", msg="We couldn't find the page you were looking for."
            ),
            404,
        )
    else:
        return (
            render_template(
                "error.html", msg="Something broke inside. We're working on fixing it."
            ),
            500,
        )


@sitemapper.include(
    lastmod="2025-01-24",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/past_work")
def past_work():
    return render_template("past_work.html")


@sitemapper.include(
    lastmod="2025-01-24",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/pcmp")
def pcmp():
    return render_template("pcmp.html")


@sitemapper.include(
    lastmod="2025-01-24",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/pcmp/dashboard")
def pcmp_dashboard():
    return render_template("pcmp_dashboard.html", repo_badges=pcmp_repo_badges())


@sitemapper.include(
    lastmod="2025-01-24",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/music")
def music():
    return render_template(
        "music.html",
        monthlies=get_ctbus_monthly_playlists(),
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


@sitemapper.include(url_variables={"project": project_list})
@app.route("/projects")
@app.route("/projects/<project>")
def projects(project=None):
    if project:
        project_info = projects_dict.get(
            project,
            {
                "title": "Uh oh!",
                "subtitle": "We can't find the metadata for this project :(",
                "tags": ["embarrassment", "shame"],
            },
        )
        return render_template(
            f"projects/{project}.html",
            title=project_info["title"],
            subtitle=project_info["subtitle"],
            tags=project_info["tags"],
            img_link=f"{CDN_URL}/images/{project_info['image']}",
        )
    return render_template("projects.html", projects=projects_dict)


@sitemapper.include(
    lastmod="2025-01-24",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/sports")
def sports():
    return render_template("sports.html", chess_stats=get_chess_stats())


@sitemapper.include(
    lastmod="2025-01-24",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/education")
def education():
    return render_template("education.html")


@sitemapper.include(
    lastmod="2025-01-24",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/certifications")
def certifications():
    return render_template("certifications.html")


@sitemapper.include(
    lastmod="2025-01-24",
    changefreq="monthly",
    priority=0.9,
)
@app.route("/about")
def about():
    return render_template("about.html")


@sitemapper.include(
    lastmod="2025-01-24",
    changefreq="monthly",
    priority=0.95,
)
@app.route("/resume")
def resume():
    return redirect(f"{CDN_URL}/documents/resume.pdf")


@app.route("/favorite-number")
def favorite_number():
    return render_template("favorite-number.html")


@app.route("/start-the-server")
def start_the_server():
    return render_template("start-the-server.html")


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
