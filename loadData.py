# load data from excel files to sqlalchemy 

import pandas as pd
from catTV import db
from catTV.models import Video, Category


videoFile = "./CatVideos.xlsx"
categoryFile = "./CatVideoCategories.xlsx"             

df = pd.read_excel(videoFile, header = 0)
df.head()

df2 = pd.read_excel(categoryFile, header = 0)
df2.head()


# TODO: improve this so not recreating table everytime
db.drop_all()
db.create_all()

# Video.query.all() to check 
for idx,row in df.iterrows():
        v = Video()
        v.id = int(df.loc[idx,"id"])
        v.url = df.loc[idx,"url"]
        v.title = df.loc[idx,"title"]
        db.session.add(v)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(str(e))

# Category.query.all() to check
for idx,row in df2.iterrows():
        c = Category()
        c.id = int(df2.loc[idx,"id"])
        c.category = df2.loc[idx,"category"]
        db.session.add(c)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(str(e))

# df.to_sql('Video', con=connection, if_exists='append', index_label="id") 
