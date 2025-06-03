from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data['name'],
                description=data['description']
            )
        )

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        {
            "name": "Pathfinder", "dealer_id": 1, "type": "SUV", "year": 2023,
            "car_make": car_make_instances[0], "motor_type": "INLINE"
        },
        {
            "name": "Qashqai", "dealer_id": 1, "type": "SUV", "year": 2023,
            "car_make": car_make_instances[0], "motor_type": "INLINE"
        },
        {
            "name": "XTRAIL", "dealer_id": 1, "type": "SUV", "year": 2023,
            "car_make": car_make_instances[0], "motor_type": "INLINE"
        },
        {
            "name": "A-Class", "dealer_id": 1, "type": "SUV", "year": 2023,
            "car_make": car_make_instances[1], "motor_type": "INLINE"
        },
        {
            "name": "C-Class", "dealer_id": 1, "type": "SUV", "year": 2023,
            "car_make": car_make_instances[1], "motor_type": "INLINE"
        },
        {
            "name": "E-Class", "dealer_id": 1, "type": "SUV", "year": 2023,
            "car_make": car_make_instances[1], "motor_type": "INLINE"
        },
        {
            "name": "A4", "dealer_id": 1, "type": "SUV", "year": 2023,
            "car_make": car_make_instances[2], "motor_type": "INLINE"
        },
        {
            "name": "A5", "dealer_id": 1, "type": "SUV", "year": 2023,
            "car_make": car_make_instances[2], "motor_type": "INLINE"
        },
        {
            "name": "A6", "dealer_id": 1, "type": "SUV", "year": 2023,
            "car_make": car_make_instances[2], "motor_type": "INLINE"
        },
        {
            "name": "Sorrento", "dealer_id": 1, "type": "SUV", "year": 2023,
            "car_make": car_make_instances[3], "motor_type": "INLINE"
        },
        {
            "name": "Carnival", "dealer_id": 1, "type": "SUV", "year": 2023,
            "car_make": car_make_instances[3], "motor_type": "INLINE"
        },
        {
            "name": "Cerato", "dealer_id": 1, "type": "Sedan", "year": 2023,
            "car_make": car_make_instances[3], "motor_type": "INLINE"
        },
        {
            "name": "Corolla", "dealer_id": 1, "type": "Sedan", "year": 2023,
            "car_make": car_make_instances[4], "motor_type": "INLINE"
        },
        {
            "name": "Camry", "dealer_id": 1, "type": "Sedan", "year": 2023,
            "car_make": car_make_instances[4], "motor_type": "INLINE"
        },
        {
            "name": "Kluger", "dealer_id": 1, "type": "SUV", "year": 2023,
            "car_make": car_make_instances[4], "motor_type": "INLINE"
        },
        # Add more CarModel instances as needed
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'], car_make=data['car_make'],
            type=data['type'], year=data['year']
        )
