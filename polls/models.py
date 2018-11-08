import datetime
from django.db import models
from django.utils import timezone


class Topic(models.Model):
    subject_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    importance_score = models.IntegerField(default=0)
    complexity_score = models.IntegerField(default=0)
    def __str__(self):
        return self.subject_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class SubTopic(models.Model):
    subject = models.ForeignKey(Topic, on_delete=models.CASCADE)
    subtopic_name = models.CharField(max_length=200)
    importance_score = models.IntegerField(default=0)
    complexity_score = models.IntegerField(default=0)
    def __str__(self):
        return self.subtopic_name


class Question(models.Model):
    quesiton_name = models.ForeignKey(SubTopic,on_delete=models.CASCADE,)
    questions = models.TextField()
    author = models.ForeignKey('auth.user',on_delete = models.CASCADE,)
    
    def __str__(self):
        return self.questions


#class Tag(models.Model):
 #   author = models.ForeignKey('auth.user',on_delete = models.CASCADE,)
    #quesiton_name = models.ForeignKey(Question,on_delete=models.CASCADE,)
  #  tags = models.CharField(max_length=1000)
    
   # def __str__(self):
    #    return self.description