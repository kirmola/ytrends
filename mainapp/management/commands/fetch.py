from os import environ
from django.core.management.base import BaseCommand
from ...models import Video
from time import sleep
from requests_cache import CachedSession
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta, date

CF_AC_ID = environ['CF_AC_ID']
CF_AUTH_TOKEN = environ['CF_AUTH_TOKEN']
AI_MODEL = environ['CF_AI_MODEL']
WORKER_URL = environ["CF_WORKER_URL"]
YT_DATA_API_BASE_URL = "https://www.googleapis.com/youtube/v3/videos"
YT_DATA_API_PARAMS = {
    "part": "snippet",
    "chart": "mostPopular",
    "regionCode": "IN",
    "maxResults": 50,
    "key": environ["YT_DATA_API_KEY"]
}

class Command(BaseCommand):

    def handle(self, *args, **options) -> str | None:
        worker_url =  WORKER_URL
        model_name = AI_MODEL

        session = CachedSession("yt_cache", expire_after=timedelta(hours=12))

        try:
            request = session.get(YT_DATA_API_BASE_URL, params=YT_DATA_API_PARAMS).json()
            response =  [{
                "video_id":each_result["id"],
                "video_detail":each_result["snippet"]
            } for each_result in request["items"]]


            result = Video(
                video_api_result = response,
                date_fetched = date.today().strftime('%Y-%m-%d')
            )
            result.save()
            self.stdout.write(self.style.SUCCESS("Results saved in database"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Can't save, something wrong: {e}"))