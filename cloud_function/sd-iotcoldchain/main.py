import json
import base64
from datetime import datetime
from google.cloud import pubsub_v1
import os

publisher = pubsub_v1.PublisherClient()

PROJECT_ID = "project-ba10611b-e217-4ef7-a94"

TEMPERATURE_TOPIC = "coldchain-temperature"
ALERT_TOPIC = "temperature-alerts"

temperature_topic_path = publisher.topic_path(PROJECT_ID, TEMPERATURE_TOPIC)
alert_topic_path = publisher.topic_path(PROJECT_ID, ALERT_TOPIC)


def ingest_temperature(request):

    if request.method != "POST":
        return ("Only POST allowed", 405)

    request_json = request.get_json(silent=True)

    if not request_json:
        return ("Invalid JSON", 400)

    device_id = request_json.get("device_id")
    temperature = request_json.get("temperature")
    timestamp = request_json.get("timestamp")
    location = request_json.get("location")
    battery_level = request_json.get("battery_level")

    event = {
        "device_id": device_id,
        "temperature": temperature,
        "timestamp": timestamp,
        "location": location,
        "battery_level": battery_level,
        "ingested_at": datetime.utcnow().isoformat() + "Z"
    }

    message = json.dumps(event).encode("utf-8")

    # Publicar en topic principal
    publisher.publish(temperature_topic_path, message)

    # Detectar anomalía
    if temperature < 2 or temperature > 8:

        alert_event = {
            "device_id": device_id,
            "temperature": temperature,
            "timestamp": timestamp,
            "location": location,
            "alert": "TEMPERATURE_OUT_OF_RANGE"
        }

        alert_message = json.dumps(alert_event).encode("utf-8")

        publisher.publish(alert_topic_path, alert_message)

    return ("Event processed", 200)