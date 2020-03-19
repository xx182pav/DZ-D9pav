from datetime import datetime
from app.models import Post, Author, Category 
from rest_framework import serializers
from django.contrib.auth.models import User

# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     slug = serializers.SlugField()
#     status = serializers.CharField(max_length=10)
#     content = serializers.CharField()
#     updated = serializers.DateTimeField()
#     publication_date = serializers.DateTimeField()
#     post_id = serializers.IntegerField()


class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:  
        model = User  
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    
    author = AuthorSerializer(required=False,read_only=True)
    category = serializers.SlugRelatedField(many=True, slug_field='slug', queryset=Category.objects.all())


    class Meta:  
        model = Post  
        fields = '__all__'
         


class CategorySerializer(serializers.ModelSerializer):

    post = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')

    class Meta:
        model = Category
        fields = '__all__'




class AuthorDetailedSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)

    class Meta:
        model = Author
        fields = '__all__'

class CategoryDetailedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'





 

    # def update(self, instance, validated_data):
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.save()
    #     return instance

  
 



