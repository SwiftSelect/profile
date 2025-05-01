from confluent_kafka import Producer
import json
import os

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "profile_updates")

producer = Producer({'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS})

def produce_profile_update(user_id, resume_url):
    message = {
        "candidate_id": user_id,
        "resume_url": resume_url
    }

    producer.produce(KAFKA_TOPIC, value=json.dumps(message))
    producer.flush()
