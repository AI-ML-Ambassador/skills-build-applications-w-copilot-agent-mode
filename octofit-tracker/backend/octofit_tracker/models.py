from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    # ...other fields...

class Team(models.Model):
    name = models.CharField(max_length=100)
    # ...other fields...

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ...other fields...

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # ...other fields...

class Workout(models.Model):
    name = models.CharField(max_length=100)
    # ...other fields...