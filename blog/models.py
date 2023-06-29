from django.db import models

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=100)
   

    def __str__(self):
        return f"{self.caption} "

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address =models.EmailField(max_length=100, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"   

    def __str__(self):
        return self.full_name()
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'



class Postdetails(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    content = models.CharField(max_length=300)
    slug =models.SlugField(unique=True)
    image_name =models.ImageField(upload_to= "images/", null=True)
    tags =models.ManyToManyField(Tag)
    
    def __str__(self):
        return f" {self.title}, {self.author}"
    
    class Meta:        
        verbose_name_plural = 'Postdetails'

class Comments(models.Model):
    user_name= models.CharField(max_length=120)
    user_email= models.EmailField()
    text=models.TextField(max_length=400)
    post =models.ForeignKey(Postdetails, on_delete=models.CASCADE, null=True , related_name ="comments")

    

    