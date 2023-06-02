from rest_framework import serializers
from .models import *


class ElevatorSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    def get_status(self, elevator):
        return f"Elevator {elevator.id} - Current Floor: {elevator.current_floor}, Running: {elevator.is_running}, Door Open: {elevator.is_door_open}, Direction: {elevator.direction}"

    class Meta:
        model = Elevator
        fields = '__all__'
        read_only_fields = ('status',)
