# elevator_problem

# Create Elevators - Endpoint to create multiple elevators at once.

URL: /elevator/create_elevators/
Method: POST
Request body example : json
{
"num_elevators": 3
}

# Send Floor Requests - Endpoint to send floor requests to the elevators.

URL: /elevator/floor_requests/
Method: POST
Request body example : json
{
"floor_requests": [11,5,2]
}

# Handle Destination Requests - Endpoint to handle destination requests for specific elevators.

URL: /elevator/destination_requests/
Method: POST
Request body example : json
{
"destination_requests": [
{
"destination_floor": 5,
"elevator_id": 1
},
{
"destination_floor": 8,
"elevator_id": 2
},
{
"destination_floor": 4,
"elevator_id": 3
}
]
}

**Models**

# Elevator

Fields:
is_operational - A boolean field indicating whether the elevator is operational.
is_door_open - A boolean field indicating whether the elevator door is open.
current_floor - An integer field representing the current floor of the elevator.
direction - A choice field indicating the direction of the elevator (UP, DOWN, or STOPPED).
Methods:
open_door(): Opens the elevator door.
close_door(): Closes the elevator door.
move_to_floor(floor): Moves the elevator to the specified floor.
**str**(): Returns a string representation of the elevator.
