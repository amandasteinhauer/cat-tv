from catTV import db


class Video(db.Model):
    __tablename__ = "video"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Video {}>'.format(self.title)

class Category(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('video.id'), primary_key=True)
    category = db.Column(db.Text, nullable=False, primary_key=True)
    

def load_videos(c):
    return Video.query.filter_by(category=c)
