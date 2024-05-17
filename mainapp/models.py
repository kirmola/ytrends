from django.db import models

from django.urls import reverse
from autoslug import AutoSlugField
from django.utils.translation import gettext_lazy as _


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

country_choices = [(code, name) for code, name in country_codes.items()]

class Video(models.Model):

    video_api_result = models.JSONField(_("API Result"), default=list)
    trending_cc = models.OneToOneField("mainapp.Country", verbose_name=_("Trending CC"), on_delete=models.CASCADE, to_field="country_code")

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")

    def __str__(self):
        return f"Youtube Trending on: {self.trending_cc}"

    def get_absolute_url(self):
        return reverse("Trendbycountry_detail", kwargs={"cc": self.trending_cc.country_code})


class Country(models.Model):

    country_code = models.CharField(_("Country Code"), max_length=2, default=None, choices=country_choices, unique=True)
    country_name = models.CharField(_("Country Name"), max_length=100, default=None)


    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countrys")

    def __str__(self):
        return self.country_name

    def get_absolute_url(self):
        return reverse("Country_detail", kwargs={"pk": self.pk})

