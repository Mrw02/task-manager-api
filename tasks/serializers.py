from rest_framework import serializers
from .models import Task, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at')
        read_only_fields = ('id', 'created_at')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class TaskSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Task
        fields = (
            'id', 'title', 'description', 'priority', 'status',
            'category', 'category_name', 'due_date', 'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_category(self, category):
        if category and category.user != self.context['request'].user:
            raise serializers.ValidationError('Category not found.')
        return category

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
