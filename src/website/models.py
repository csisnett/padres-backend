from django.contrib.auth.models import AbstractUser
from django.db import models


#remember to use settings.AUTH_USER_MODEL instead
#of User for relations (FK, One-To-One, etc)

class User(AbstractUser):
    pass




