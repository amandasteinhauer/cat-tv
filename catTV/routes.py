from flask import render_template, url_for, request
from catTV import app
from catTV.models import Video, Category

@app.route("/")
@app.route('/index')
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/videos")
def videos():
    page = request.args.get('page', 1, type=int)
    category = request.args.get('category', "All", type=str)
    if category and not category == None and category != "All":
        ids = Category.query.with_entities(Category.id).filter(Category.category == category).order_by(Category.id.desc())
    else:
        ids = Video.query.with_entities(Video.id)
    print(ids)
    print(category)
    videos = Video.query.filter(Video.id.in_(ids)).paginate(page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('videos', page=videos.next_num) if videos.has_next else None
    prev_url = url_for('videos', page=videos.prev_num) if videos.has_prev else None
    return render_template('videos.html',  videos=videos.items, next_url=next_url, prev_url=prev_url, category=category)


@app.route("/games")
def games():
    return render_template('games.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

