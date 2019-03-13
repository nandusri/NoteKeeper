from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe
from markdown import markdown

class Note(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def get_content_as_markdown(self):
  		return mark_safe(markdown(self.text, safe_mode='escape'))
        