from rest_framework import serializers

class UserInputSerializer(serializers.Serializer):
    user_input = serializers.CharField(max_length=1000)
    
    def validate_user_input(self, value):
        if not value:
            raise serializers.ValidationError("user_input is required")
        return value
    