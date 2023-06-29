from django.contrib import admin
from .models import Author, Postdetails , Tag , Comments

# Register your models here.

class PostdetailsAdmin(admin.ModelAdmin):
    list_filter=("author","tags")
    list_display = ["title","author", "content"]
    prepopulated_fields ={"slug" :("title" ,)}

class CommentAdmin(admin.ModelAdmin):
    
    list_display = ["user_name","post"]
    

admin.site.register(Author)
admin.site.register(Postdetails,PostdetailsAdmin)
admin.site.register(Tag)
admin.site.register(Comments, CommentAdmin)