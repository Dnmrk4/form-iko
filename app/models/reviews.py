Class Review:

 all_reviews = []

def __init__(self,event_id,title,imageurl,review):
    self.event_id = event_id
    self.title = title
    self.imageurl = imageurl
    self.review = review


@classmethod
def get_reviews(cls,id):

    responce = []
    
 