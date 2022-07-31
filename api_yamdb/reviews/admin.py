from django.contrib import admin
from reviews.models import Category, Genre, Title, Comment, Review

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Title)
admin.site.register(Comment)
admin.site.register(Review)
