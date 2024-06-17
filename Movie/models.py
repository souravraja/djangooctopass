from django.db import models

# Create your models here.

catagory=(
('',''),
('Horror','Horror'),
('Action','Action'),
('Thriller','Thriller'),
('Drama','Drama'),
('Romance','Romance'),
('Western','Western'),
('Science fiction','Science fiction'),
('Crime film','Crime film'),
('Documentary','Documentary'),
('Comedy','Comedy'),
('Fantasy','Fantasy'),
('Animation','Animation'),
('Adventure','Adventure'),
('Experimental','Experimental'),
('Historical film','Historical film'),
('Comedy','Comedy'),
('Drama','Drama'),
('Noir','Noir'),
('Musical','Musical'),
('Television','Television'),
('Historical Fiction','Historical Fiction'),
('Slasher','Slasher'),
('Splatter','Splatter'),
('Science fiction','Science fiction'),
('Narrative','Narrative'),
('Thriller','Thriller'),
('Satire','Satire'),
('Fantasy','Fantasy'),
('Romantic comedy','Romantic comedy'),
('History','History'),
('War','War'),
('Spaghetti western','Spaghetti western'),
('LGBT','LGBT'),
('Exploitation','Exploitation'),
('Apocalyptic and post-apocalyptic fiction','Apocalyptic and post-apocalyptic fiction'),
('Blaxploitation','Blaxploitation'),
('Sexploitation','Sexploitation'),
('Magical Realism','Magical Realism'),
('B','B'),
('Art','Art'),
('abstract animation film','abstract animation film'),
('',''),
('Indie film','Indie film'),
('',''),
('Visual album','Visual album'),
('Kaiju','Kaiju'),
('Children\'s film','Children\'s film'),
('Animated film','Animated film'),
('Punk rock','Punk rock'),
('Historical drama','Historical drama'),
)

catagory_title=[
    ('poster','poster'),
    ('Popular','Popular Movie'),
    ('New-Movie','New Movie'),
    ('hollywood','hollywood Movie'),
    ('hindi','hindi Movie'),
    ('Bangoli','Bangoli Movie'),
    ('Hindi-Dub','Hindi Dub Movie'),
]
topt=[
    ('trending','trending'),
    ('explore','explore'),
    ('favourite','favourite')
]
class movie(models.Model):
    movie_name=models.CharField(max_length=300)
    movie_descrition=models.TextField()
    movie_catagory_title=models.CharField(max_length=100,choices=catagory_title,default=0)
    movie_type=models.CharField(max_length=103, choices=catagory,default=0)
    movie_select=models.CharField(max_length=103, choices=topt,default=0,blank=True)
    movie_upload_time=models.DateTimeField(auto_now_add=True)
    movie_title_image=models.ImageField(upload_to='movie/movieTitle',blank=True)
    movie_file=models.URLField(max_length=3000,blank=True,default=None)
    movie_download_file=models.URLField(max_length=3000,blank=True,default=None)
    def __str__(self):
        return self.movie_name 