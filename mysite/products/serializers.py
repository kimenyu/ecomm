from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        read_only_fields = ('id',)

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Include the CategorySerializer here

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'category', 'stock', 'image', 'created_at')
        read_only_fields = ('id', 'created_at')

    def create(self, validated_data):
        category_data = validated_data.pop('category', None)
        if category_data:
            category, created = Category.objects.get_or_create(**category_data)
            validated_data['category'] = category
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        category_data = validated_data.pop('category', None)
from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        read_only_fields = ('id',)  # Mark 'id' field as read-only

class ProductSerializer(serializers.ModelSerializer):
    # Include the CategorySerializer here to serialize the 'category' field
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'category', 'stock', 'image', 'created_at')
        read_only_fields = ('id', 'created_at')  # Mark 'id' and 'created_at' fields as read-only

    def create(self, validated_data):
        # Handle 'category' data when creating a new product
        category_data = validated_data.pop('category', None)

        if category_data:
            # Get or create a Category instance based on the provided data
            category, created = Category.objects.get_or_create(**category_data)
            validated_data['category'] = category

        # Create a new Product instance with the validated data
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Handle 'category' data when updating an existing product
        category_data = validated_data.pop('category', None)

        if category_data:
            # Get or create a Category instance based on the provided data
            category, created = Category.objects.get_or_create(**category_data)
            instance.category = category

        # Update other fields based on validated data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Save and return the updated Product instance
        instance.save()
        return instance

        if category_data:
            category, created = Category.objects.get_or_create(**category_data)
            instance.category = category

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
