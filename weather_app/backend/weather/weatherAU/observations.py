from .. import weatherAU

# https://docs.python.org/3/library/xml.dom.html#module-xml.dom

class Observations:

    def __init__(self, state=None):

        if not state:
            state = weatherAU.api.WeatherApi().search(weatherAU.api.WeatherApi().q)[0]

        self.state = (state['state'].lower()).capitalize()
        self.url = weatherAU.OBSERVATION_PRODUCT_URL[self.state]
        self.soup = weatherAU.fetch_xml(self.url)
        self.identifier = self.soup.identifier.contents[0]
        self.acknowedgment = f'Data courtesy of Bureau of Meteorology ({self.url})'
    

    def stations(self):
        # List of station attributes

        station_list =[]

        for station in self.soup.find_all('station'):
            station_list.append(station.attrs)

        return station_list

    def get_wmo_id(self, location=None):
        # Get an wmo_id given the location

        stations = self.stations()

        for station in stations:
            if station['description'] == location['name']:
                return station['wmo-id']
            if station['lat'] == location['latitude'] and station['lon'] == location['longitude']:
                return station['wmo-id']
            if station['description'] == location['timezone'].split('/')[1].replace('_', ' '):
                return station['wmo-id']
        return None

    def station_elements(self, wmo_id=None):
        # Element child tags for a specified station

        return self.soup.find('station', {'wmo-id': wmo_id})


    def station_attribute(self, wmo_id=None, attribute=None):

        attrs = self.soup.find('station', {'wmo-id': wmo_id}).attrs

        if attribute in attrs:
            return attrs[attribute]
        else:
            return None


    def period_attribute(self, wmo_id=None, attribute=None):

        elements = self.soup.find('station', {'wmo-id': wmo_id})

        attrs = elements.find('period').attrs

        if attribute in attrs:
            return attrs[attribute]
        else:
            return None


    def air_temperature(self, wmo_id=None):
        """ Don't assume that any elements exist or that there is an element with type air_temperature
        """

        elements = self.soup.find('station', {'wmo-id': wmo_id})
        
        if elements is not None:
            air_temperature_el = elements.find('element', {'type': 'air_temperature'})

            if air_temperature_el is not None and len(air_temperature_el.contents) > 0:
                    return air_temperature_el.contents[0]

        return None

    def rainfall(self, wmo_id=None):
        """ Don't assume that any elements exist or that there is an element with type rainfall
        """

        elements = self.soup.find('station', {'wmo-id': wmo_id})

        if elements is not None:
            rainfall_el = elements.find('element', {'type': 'rainfall'})

            if rainfall_el is not None and len(rainfall_el.contents) > 0:
                    return rainfall_el.contents[0]

        return None

    def __str__(self):
        return str(self.soup)
