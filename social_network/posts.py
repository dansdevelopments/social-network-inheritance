from datetime import datetime

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp
        self.user = None

    def set_user(self, user):
        self.user = user
    
    @classmethod
    def get_timestamp(cls, post):
        return post.timestamp

class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super().__init__(text, timestamp)

    def __str__(self):
        return_str = "@{} {}: ".format(self.user.first_name, self.user.last_name)
        return_str += '"{}"\n\t'.format(self.text)
        return_str += self.timestamp.strftime("%A, %b %d, %Y")
        return return_str
        # '@Kevin Watson: "Sample post text"\n\tTuesday, Jan 10, 2017'


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super().__init__(text,timestamp)
        self.image_url = image_url

    def __str__(self):
        return_str = "@{} {}: ".format(self.user.first_name, self.user.last_name)
        return_str += '"{}"\n\t'.format(self.text)
        return_str += self.image_url + "\n\t"
        return_str += self.timestamp.strftime("%A, %b %d, %Y")
        return return_str
        # '@Kevin Watson: "Sample post text"\n\thttp://fake-domain.com/images/sample.jpg\n\tTuesday, Jan 10, 2017'


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super().__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return_str = "@{} Checked In: ".format(self.user.first_name)
        return_str += '"{}"\n\t'.format(self.text)
        return_str += str(self.latitude) + ", " + str(self.longitude) + "\n\t"
        return_str += self.timestamp.strftime("%A, %b %d, %Y")
        return return_str
        # '@Kevin Checked In: "Sample post text"\n\t-34.603722, -58.381592\n\tTuesday, Jan 10, 2017'
