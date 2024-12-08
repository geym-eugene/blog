from datetime import date

from rest_framework import serializers
from blog.models import Post, Comment
from blog.validators import TitleValidator


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[TitleValidator()])

    class Meta:
        model = Post
        fields = ['id', 'title', 'text']

    def validate(self, data):
        # Получаем пользователя из контекста запроса
        user = self.context.get('request').user  # текущий авторизованный пользователь

        if user:
            # Проверка возраста пользователя
            today = date.today()
            age = today.year - user.birth_date.year - (
                        (today.month, today.day) < (user.birth_date.month, user.birth_date.day))
            if age < 18:
                raise serializers.ValidationError("Автор поста должен быть старше 18 лет.")

        return data

    def create(self, validated_data):
        # Устанавливаем автором текущего пользователя
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "author", "text", "created_at", "updated_at"]