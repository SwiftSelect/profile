from confluent_kafka import Producer
import json
import os

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_SASL_USERNAME = os.getenv("KAFKA_SASL_USERNAME", "admin")
KAFKA_SASL_PASSWORD = os.getenv("KAFKA_SASL_PASSWORD", "admin")
KAFKA_CLIENT_ID = os.getenv("KAFKA_CLIENT_ID", "profile_updates_client")

config = {
    "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
    "client.id": KAFKA_CLIENT_ID,
    "security.protocol": "SASL_SSL",
    "sasl.mechanisms": "PLAIN",
    "sasl.username": KAFKA_SASL_USERNAME,
    "sasl.password": KAFKA_SASL_PASSWORD,
    "session.timeout.ms": 45000,
}

producer = Producer(config)

def produce_profile_update(user_id, resume_url):
    message = {
        "candidate_id": user_id,
        "resume_url": resume_url
    }

    producer.produce("candidate_topic", value=json.dumps(message))
    producer.flush()
