from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]

class Lecture(models.Model):
    subject = models.CharField(max_length=100)
    dept = models.CharField(max_length=150)
    professor = models.CharField(max_length=50)
    instruction_id = models.CharField(max_length=100)
    rq_year = models.CharField(max_length=150)
    rq_semester = models.CharField(max_length = 100)
    area = models.CharField(max_length = 100)
    url = models.CharField(max_length = 100)
    credit = models.CharField(max_length = 100)
    class_time = models.CharField(max_length=100)
    required = models.BooleanField()    
    foreigner = models.BooleanField()
    team_teaching = models.BooleanField()
    mooc = models.BooleanField()
    online = models.BooleanField()
    number_of_people = models.CharField(max_length=100)
    note = models.CharField(max_length=100)

    def __str__(self):
        return self.subject

class Signup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    std_num = models.CharField(max_length=50)
    major = models.CharField(max_length=100)
    name = models.CharField(max_length=200)