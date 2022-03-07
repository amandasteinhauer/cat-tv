from flask import render_template, url_for, request
from catTV import app, models

@app.route("/")
@app.route('/index')
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/birds")
def birds():
    page = request.args.get('page', 1, type=int)
    videos = models.Video.query.order_by(models.Video.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('birds', page=videos.next_num) if videos.has_next else None
    prev_url = url_for('birds', page=videos.prev_num) if videos.has_prev else None
    return render_template('videos.html',  videos=videos.items, next_url=next_url, prev_url=prev_url)


@app.route("/games")
def games():
    return render_template('games.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

