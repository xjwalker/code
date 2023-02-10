from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    image = models.TextField()
    video = models.TextField()
    audio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Story(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    grid_x_size = models.IntegerField(null=True)
    grid_y_size = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    events = models.ManyToManyField(Event, through='Plot')

    def __str__(self):
        return self.name


class Plot(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    x_position = models.IntegerField(null=False)
    y_position = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Timeline(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    stories = models.ManyToManyField(Story)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
