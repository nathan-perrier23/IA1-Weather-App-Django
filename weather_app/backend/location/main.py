import requests
from requests import get
from decouple import config
from django.core.cache import cache
from requests.exceptions import ReadTimeout

from .models import UserLocationModel

class GetLocation:
    def __init__(self):
        pass

    def get_location(self):
        ip_address = self.get_ip_address()
        if ip_address is not None:
            if UserLocationModel.objects.filter(ip=ip_address).exists() == False:
                print('ip address:', ip_address)
                try:
                    location_info = get(f'http://ip-api.com/json/{str(ip_address)}', timeout=5).json()
                    if location_info['status'] == 'success':
                        return self.store_user_location(location_info, ip_address)
                    return None
                except ReadTimeout: return None
            return UserLocationModel.objects.get(ip=ip_address)
        return None
        
    def get_ip_address(self):
        try:
            return get('https://api.ipify.org?format=json', timeout=5).json()['ip']
        except ReadTimeout:
            return None
        
    def store_user_location(self, location, ip):
        return UserLocationModel.objects.create(
            ip=ip, 
            city=location['city'], 
            region=location['region'], 
            region_name=location['regionName'], 
            country=location['country'], 
            timezone=location['timezone'], 
            lat=location['lat'], 
            lon=location['lon'],
            zip=location['zip'],
            country_code=location['countryCode'],
            isp=location['isp']
        )
        
        