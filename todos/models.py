from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Board(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(
        get_user_model(), 
        on_delete=models.PROTECT, 
        related_name="owned_boards"
    )
    members = models.ManyToManyField(get_user_model(), related_name="boards")

    def __str__(self):
        return self.name

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        is_new = self.pk is None
        super().save(force_insert, force_update, using, update_fields)
        if is_new:
            self.members.add(self.owner)
    
    def get_absolute_url(self):
        return reverse('board_detail', args=[str(self.id)])


class Column(models.Model):
    title = models.CharField(max_length=255)
    board = models.ForeignKey(Board, related_name="columns", on_delete=models.CASCADE)
    column_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ["column_order"]

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('board_detail', args=[str(self.id)])


class Label(models.Model):
    name = models.CharField(max_length=255)
    board = models.ForeignKey("Board", related_name="labels", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name", "board"], name="unique_name_board")
        ]

class Priority(models.TextChoices):
    HIGH = "H", "High"
    MEDIUM = "M", "Medium"
    LOW = "L", "Low"


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    priority = models.CharField(
        max_length=1, choices=Priority.choices, default=Priority.MEDIUM
    )
    labels = models.ManyToManyField(Label, related_name="tasks")
    assignees = models.ManyToManyField(get_user_model(), related_name="tasks")
    column = models.ForeignKey(Column, related_name="tasks", on_delete=models.CASCADE)
    task_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return f"{self.id} - {self.title}"

    class Meta:
        ordering = ["task_order"]

    def get_absolute_url(self):
        return reverse('board')


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name="comments")
    text = models.TextField()

