from django.db import models


class Elevator(models.Model):
    DIRECTION_CHOICES = (
        ('UP', 'Up'),
        ('DOWN', 'Down'),
        ('STOPPED', 'Stopped')
    )

    is_operational = models.BooleanField(default=True)
    is_door_open = models.BooleanField(default=False)
    current_floor = models.PositiveIntegerField(default=1)
    direction = models.CharField(
        max_length=10, choices=DIRECTION_CHOICES, default='STOPPED')

    def open_door(self):
        if not self.is_door_open:
            self.is_door_open = True
            self.save()

    def close_door(self):
        if self.is_door_open:
            self.is_door_open = False
            self.save()

    def move_to_floor(self, floor):
        if self.current_floor is not None:
            if floor > self.current_floor:
                self.direction = 'UP'
            elif floor < self.current_floor:
                self.direction = 'DOWN'
            else:
                self.direction = 'STOPPED'
        self.current_floor = floor
        self.save()

    def __str__(self):
        return f"Elevator {self.id}"
