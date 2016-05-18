
import webbrowser

class DjSet():
    def __init__(self, djset_artist, djset_description, poster_image, trailer_youtube):
        self.title = djset_artist
        self.storyline = djset_description
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    def show_youtube(self):
        webbrowser.open(self.trailer_youtube_url)        
