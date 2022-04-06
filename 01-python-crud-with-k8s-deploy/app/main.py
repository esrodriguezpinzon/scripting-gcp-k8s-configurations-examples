import json
from typing import Optional
from logging import exception
from google.cloud import pubsub_v1
from fastapi import FastAPI, Request, Response

app = FastAPI()

project_id = "your-project-id"
topic_id = "your-topic-id"

publisher = pubsub_v1.PublisherClient()

@app.get("/", status_code=200)
def read_root():
    return {"Message": "Request received"}

@app.get("/healthcheck", status_code=200)
def healthcheck():
    return {"Message": "Hey, We are alive!"}

@app.post("/send-a-pubsub-event/", status_code=201)
async def ml_solver_test(request: Request, response: Response):
    try:
        topic_path = publisher.topic_path(project_id, topic_id)
        income_request_body = await request.json() # All the params required to run
        pub_sub_request = json.dumps(income_request_body).encode("utf-8")
        pub_sub_event = publisher.publish(topic_path, pub_sub_request)
        result_resp = {
            "event_published": pub_sub_event.result(),
            "body_sent": income_request_body
        }
        return result_resp
    except exception as e:
        print("Error: " + str(e))
        response.status_code =404
        return {"Message": "Request received with error"}
