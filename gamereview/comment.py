from google.appengine.ext import ndb

class Comment(ndb.Model):
    game = ndb.KeyProperty()
    user = ndb.StringProperty()
    numHours = ndb.IntegerProperty()
    finished = ndb.BooleanProperty()
    comment = ndb.StringProperty(required = True)
    punctuation = ndb.IntegerProperty()
    date = ndb.DateProperty(auto_now_add = True)