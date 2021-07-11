from django.db import models


from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
class UserExtensionModel(models.Model):
	user = models.OneToOneField(User,on_delete=CASCADE,related_name='extension')
	sex = models.CharField('sex',max_length=10)
	photo = models.ImageField('face_image')
	age = models.IntegerField('age')
	

	def __str__(self):
		return self.user.username
