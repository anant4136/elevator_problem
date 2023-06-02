from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *


class ElevatorView(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    @action(detail=False, methods=['post'])
    def create_elevators(self, request):
        num_elevators = request.data.get('num_elevators', 0)
        elevators = []
        for _ in range(num_elevators):
            elevator = Elevator()
            elevator.save()
            elevators.append(elevator)

        serializer = self.get_serializer(elevators, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def process_requests(self, request):
        floor_requests = request.data.get('floor_requests', [])
        for floor in floor_requests:
            closest_elevator = self.find_closest_elevator(floor)
            if closest_elevator:
                closest_elevator.move_to_floor(floor)
                self.remove_request(floor)

        elevators = self.get_queryset()
        serializer = self.get_serializer(elevators, many=True)
        return Response(serializer.data)

    def find_closest_elevator(self, floor):
        elevators = Elevator.objects.filter(
            is_operational=True, is_door_open=False)
        if not elevators:
            return None
        closest_elevator = elevators[0]
        closest_distance = abs(floor - closest_elevator.current_floor)
        for elevator in elevators[1:]:
            distance = abs(floor - elevator.current_floor)
            if distance < closest_distance:
                closest_elevator = elevator
                closest_distance = distance
        return closest_elevator
