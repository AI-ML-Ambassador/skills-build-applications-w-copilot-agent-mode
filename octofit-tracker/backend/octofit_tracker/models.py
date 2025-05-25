from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'octofit'

class Team(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'octofit'

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        app_label = 'octofit'

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        app_label = 'octofit'

class Workout(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'octofit'