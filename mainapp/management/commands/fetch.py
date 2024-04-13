from os import environ
from django.core.management.base import BaseCommand
from ...models import Question
from time import sleep
import requests
from concurrent.futures import ThreadPoolExecutor

CF_AC_ID = environ['CF_AC_ID']
CF_AUTH_TOKEN = environ['CF_AUTH_TOKEN']
AI_MODEL = environ['CF_AI_MODEL']
WORKER_URL = environ["CF_WORKER_URL"]

class Command(BaseCommand):

    def handle(self, *args, **options) -> str | None:
        worker_url =  WORKER_URL
        model_name = AI_MODEL

        questions = [each.question for each in Question.objects.all()]

        for each_quest in questions[:5]:
            data = {
                "query":each_quest,
                "model":model_name
            }
            response = requests.post(worker_url, json=data)
            print(response.json())

        # def send_request(question):
        #         try:
        #             data = {
        #                     "query": question,
        #                     "model": model_name
        #             }
        #             response = requests.post(worker_url, json=data)
        #             response.raise_for_status()
        #             filename = f"{question}.txt"
        #             with open(filename, "w") as f:
        #                 f.write(response.text)
        #             return self.stdout.write(self.style.SUCCESS(f"Request done for: {question}"))
        #         except requests.exceptions.RequestException as e:
        #             self.stdout.write(self.style.ERROR(f"Failed for: {question}"))
                

        # with ThreadPoolExecutor(max_workers=3) as executor:
        #     results = executor.map(send_request, questions)
        #     print(results.result())
