from ..__init__ import *

class RetrieveForecast():
    def __init__(self, request):
        self.request = request
        
        self.data = uv_index.UVIndex(self.request.location())  #? location works? if not parse state into class and use that
        self.accumulative_list = self.data.acc_list()

    def get_uv_descriptions(self):
        return [desc for desc in self.accumulative_list]
    
    def get_uv_message(self):
        return self.data.uv_message(self.accumulative_list)  #? works
        
        # location_name = 'Melbourne'
        # uv_message = uv_data.uv_message(uv_data.get_aac(location_name))

        # print('\nUV Message for', location_name, uv_message)