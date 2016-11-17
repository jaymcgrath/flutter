from django.db import models

# Create your models here.

class Flutt(models.Model):
    """
    Basic model for a microblog entry
    """
    author = models.CharField(max_length=69)
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        formatted = "{author}:{body}"
        return formatted.format(author=self.author, body=self.body[:36])
