from django.db import models

class Song(models.Model):
    title = models.TextField()
    artist = models.TextField()
    image = models.ImageField()
    audio_file = models.FileField(blank=True, null=True)
    audio_link = models.CharField(max_length=200, blank=True, null=True)
    duration = models.CharField(max_length=20)

    paginate_by = 2

    def __str__(self):
        return self.title

    def get_download_url(self):
        if self.audio_file:
            return self.audio_file.url
        elif self.audio_link:
            return self.audio_link
        else:
            return None
