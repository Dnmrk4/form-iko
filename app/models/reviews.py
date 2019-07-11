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
    for review in cls.all_reviews:
        if review.event_id == id:
            responce.append(review)
            return responce


def save_reviews(self):
    Review.all_reviews.append(self) 


@classmethod
def clear_reviews(cls):
    Review.all_reviews.clear()
 