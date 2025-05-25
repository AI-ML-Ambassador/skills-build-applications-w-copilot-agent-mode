from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Test data for users
        users = [
            {"email": "user1@example.com", "name": "User One"},
            {"email": "user2@example.com", "name": "User Two"},
        ]
        db.users.insert_many(users)

        # Test data for teams
        teams = [
            {"name": "Team Alpha"},
            {"name": "Team Beta"},
        ]
        db.teams.insert_many(teams)

        # Test data for activities
        activities = [
            {"user": "user1@example.com", "activity": "Running", "duration": 30},
            {"user": "user2@example.com", "activity": "Cycling", "duration": 45},
        ]
        db.activity.insert_many(activities)

        # Test data for leaderboard
        leaderboard = [
            {"team": "Team Alpha", "points": 100},
            {"team": "Team Beta", "points": 80},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Test data for workouts
        workouts = [
            {"name": "Workout A", "description": "Full body workout"},
            {"name": "Workout B", "description": "Cardio workout"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
