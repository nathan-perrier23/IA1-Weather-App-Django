from .__init__ import *
from ..models import LocationImagesModel
from ..visionAI import VisionAIModel
from django.core.files.base import ContentFile

class GenerateLocationImage:
    def __init__(self, location):
        self.location = location

    def generate(self):
        response = client.images.generate(
            model=MODEL,
            prompt=f'{self.location.city}, {self.location.region}, {self.location.zip}, {self.location.country}',
            size="1024x1024",
            style="natural", #natural or vivid
            quality="hd", #standard
            n=1,
        )
        return self.save_image(response.data[0].url)
        # print(FILE_PATH)
        # return self.save_image('https://oaidalleapiprodscus.blob.core.windows.net/private/org-mZwyRow8Epk0kqfzKFmqI3Ki/user-vMp0uddvjlLDJLZMfzXQztu8/img-c6BypJmDSpMhHSpmVsB3bYUB.png?st=2024-01-14T05%3A46%3A12Z&se=2024-01-14T07%3A46%3A12Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-01-14T02%3A42%3A46Z&ske=2024-01-15T02%3A42%3A46Z&sks=b&skv=2021-08-06&sig=WedVWJskG6fx3FYz2cCeu74qfkkbwjq7IipKLZe5fEA%3D')
    
    def get_image(self):
        LocationImagesModel.objects.filter(city=self.location.city).delete()
        if LocationImagesModel.objects.filter(city=self.location.city).exists():
            return LocationImagesModel.objects.get(city=self.location.city)
        return self.generate()
        

    def save_image(self, url):

        file_name = str(uuid.uuid4()) + '.png'

        file_name = self.check_dir(os.path.join(FILE_PATH, file_name))
        
        # if VisionAIModel(directory).is_image_safe():
        image = self.add_image_to_db(file_name=file_name, response=requests.get(url))
        return image
    
    def add_image_to_db(self, response, file_name):
        self.location_image = LocationImagesModel(
            country=self.location.country,
            city=self.location.city,
            zip=self.location.zip,
            lat=self.location.lat,
            lon=self.location.lon,
            is_safe=True
        )
        self.location_image.image_url.save(file_name, ContentFile(response.content), save=True)
        return self.location_image

    def generate_name(self, length=50):
        # generate a random name for the image
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    
    def check_dir(self, directory):
        # check if the directory exists
        if os.path.exists(directory): 
            return self.check_dir((FILE_PATH + self.generate_name() + '.png')).split(FILE_PATH)[1]
        return directory.split(FILE_PATH)[1]
