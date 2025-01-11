from django.contrib import admin

# Register your models here.
@admin.register(movies)
class moviesAdmin(admin.ModelAdmin):
    pass
@admin.register(user)
class userAdmin(admin.ModelAdmin):
    pass