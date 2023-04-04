from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class HackathonOrganizers(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

# Title
# description
# Background image
# Hackathon image
# type of submission - Only one of these types should be selected while creating the hackathon - image, file or a link. You can assume that this field cannot be changed after the hackathon has started.
# Start datetime
# End datetime
# Reward prize

class Hackathons(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    background_image = models.CharField(max_length=100)
    hackathon_image = models.CharField(max_length=100)
    type_of_submission = models.CharField(max_length=100)
    start_datetime = models.DateTimeField(auto_now_add=True)
    end_datetime = models.DateTimeField(auto_now_add=True)
    reward_prize = models.CharField(max_length=100)
    organized_by = models.ForeignKey(HackathonOrganizers, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

class HackathonRegistry(models.Model):
    hackathon_id = models.ForeignKey(Hackathons, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

class HackathonSubmissions(models.Model):
    hackathon_id = models.ForeignKey(Hackathons, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    summary = models.CharField(max_length=100)
    submission_type = models.CharField(max_length=100)
    submission_file = models.FileField(upload_to='file_upload/')
    # submission_image = models.ImageField(upload_to='images_upload/')
    submission_url = models.URLField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
