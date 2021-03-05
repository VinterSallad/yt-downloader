import pytube


class Downloader:

    #
    def __init__(self, url):
        self.youtube = pytube.YouTube(url)

    #
    def download(self, directory):
        video = self.youtube.streams.get_highest_resolution()
        video.download(directory)

    #
    def get_info(self):
        author = self.youtube.author
        title = self.youtube.title
        desc = self.youtube.description
        date = self.youtube.publish_date

        views = self.youtube.views
        length = self.youtube.length
        rating = self.youtube.rating
