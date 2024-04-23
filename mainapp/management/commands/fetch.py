from os import environ
from django.core.management.base import BaseCommand
from ...models import Video, Country
from time import sleep
from requests_cache import CachedSession
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import timedelta, date


# CF_AC_ID = environ['CF_AC_ID']
# CF_AUTH_TOKEN = environ['CF_AUTH_TOKEN']
# AI_MODEL = environ['CF_AI_MODEL']
# WORKER_URL = environ["CF_WORKER_URL"]
YT_DATA_API_BASE_URL = "https://www.googleapis.com/youtube/v3/videos"
YT_DATA_API_PARAMS = {
    "part": ["snippet", "statistics"],
    "chart": "mostPopular",
    "maxResults": 50,
    "key": environ["YT_DATA_API_KEY"]
}

country_codes = {
    'AL': 'Albania',
    'AE': 'United Arab Emirates',
    'AR': 'Argentina',
    'AM': 'Armenia',
    'AU': 'Australia',
    'AT': 'Austria',
    'AZ': 'Azerbaijan',
    'BE': 'Belgium',
    'BD': 'Bangladesh',
    'BG': 'Bulgaria',
    'BH': 'Bahrain',
    'BA': 'Bosnia and Herzegovina',
    'BY': 'Belarus',
    'BO': 'Bolivia, Plurinational State of',
    'BR': 'Brazil',
    'CA': 'Canada',
    'CH': 'Switzerland',
    'CL': 'Chile',
    'CO': 'Colombia',
    'CR': 'Costa Rica',
    'CY': 'Cyprus',
    'CZ': 'Czechia',
    'DE': 'Germany',
    'DK': 'Denmark',
    'DO': 'Dominican Republic',
    'DZ': 'Algeria',
    'EC': 'Ecuador',
    'EG': 'Egypt',
    'ES': 'Spain',
    'EE': 'Estonia',
    'FI': 'Finland',
    'FR': 'France',
    'GB': 'United Kingdom',
    'GE': 'Georgia',
    'GH': 'Ghana',
    'GR': 'Greece',
    'GT': 'Guatemala',
    'HK': 'Hong Kong',
    'HN': 'Honduras',
    'HR': 'Croatia',
    'HU': 'Hungary',
    'ID': 'Indonesia',
    'IN': 'India',
    'IE': 'Ireland',
    'IQ': 'Iraq',
    'IS': 'Iceland',
    'IL': 'Israel',
    'IT': 'Italy',
    'JM': 'Jamaica',
    'JO': 'Jordan',
    'JP': 'Japan',
    'KZ': 'Kazakhstan',
    'KE': 'Kenya',
    'KH': 'Cambodia',
    'KR': 'Korea, Republic of',
    'KW': 'Kuwait',
    'LA': 'Lao People\'s Democratic Republic',
    'LB': 'Lebanon',
    'LY': 'Libya',
    'LI': 'Liechtenstein',
    'LK': 'Sri Lanka',
    'LT': 'Lithuania',
    'LU': 'Luxembourg',
    'LV': 'Latvia',
    'MA': 'Morocco',
    'MD': 'Moldova, Republic of',
    'MX': 'Mexico',
    'MK': 'North Macedonia',
    'MT': 'Malta',
    'ME': 'Montenegro',
    'MN': 'Mongolia',
    'MY': 'Malaysia',
    'NG': 'Nigeria',
    'NI': 'Nicaragua',
    'NL': 'Netherlands',
    'NO': 'Norway',
    'NP': 'Nepal',
    'NZ': 'New Zealand',
    'OM': 'Oman',
    'PK': 'Pakistan',
    'PA': 'Panama',
    'PE': 'Peru',
    'PH': 'Philippines',
    'PG': 'Papua New Guinea',
    'PL': 'Poland',
    'PR': 'Puerto Rico',
    'PT': 'Portugal',
    'PY': 'Paraguay',
    'QA': 'Qatar',
    'RO': 'Romania',
    'RU': 'Russian Federation',
    'SA': 'Saudi Arabia',
    'SN': 'Senegal',
    'SG': 'Singapore',
    'SV': 'El Salvador',
    'RS': 'Serbia',
    'SK': 'Slovakia',
    'SI': 'Slovenia',
    'SE': 'Sweden',
    'TH': 'Thailand',
    'TN': 'Tunisia',
    'TR': 'Türkiye',
    'TW': 'Taiwan, Province of China',
    'TZ': 'Tanzania, United Republic of',
    'UG': 'Uganda',
    'UA': 'Ukraine',
    'UY': 'Uruguay',
    'US': 'United States',
    'VE': 'Venezuela, Bolivarian Republic of',
    'VN': 'Viet Nam',
    'YE': 'Yemen',
    'ZA': 'South Africa',
    'ZW': 'Zimbabwe'
}



def fetch_video_data(cc):
    session = CachedSession("yt_cache", expire_after=timedelta(hours=12))
    try:
        YT_DATA_API_PARAMS.update({
            "regionCode": cc
        })
        request = session.get(YT_DATA_API_BASE_URL, params=YT_DATA_API_PARAMS).json()
        response = [{
            "video_id": each_result["id"],
            "video_detail": each_result["snippet"],
            "stats": each_result["statistics"]
        } for each_result in request["items"]]
        
        country_instance, created = Country.objects.get_or_create(country_code=str(cc).lower(), defaults={'country_name': country_codes[cc]})
        videos = Video.objects.filter(trending_cc=country_instance)
        if videos.exists():
            videos.update(video_api_result=response)
        else:
            result = Video(
                video_api_result=response,
                trending_cc=country_instance
            )
            result.save()
        return cc, True
    except Exception as e:
        print(e)
        return cc, False


class Command(BaseCommand):
    def handle(self, *args, **options):
        # worker_url = WORKER_URL
        # model_name = AI_MODEL

        with ThreadPoolExecutor(max_workers=50) as executor:
            futures = [executor.submit(fetch_video_data, cc) for cc in country_codes.keys()]
            for future in as_completed(futures):
                cc, success = future.result()
                if success:
                    self.stdout.write(self.style.SUCCESS(f"Successfully fetched data for {country_codes[cc]}"))
                else:
                    self.stdout.write(self.style.ERROR(f"Failed to fetch data for {country_codes[cc]}"))
        self.stdout.write(self.style.SUCCESS("All requests completed"))