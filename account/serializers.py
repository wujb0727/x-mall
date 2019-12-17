from rest_framework import serializers
from rest_framework.authtoken.models import Token

from account.models import User


class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension,)

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class UserAvatarSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = User
        fields = ('id', 'username', 'image')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'mobile', 'image')


class NewUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    # def create(self, validated_data):
    #     # # 重写ModelSerializer的create()方法以保存User实例
    #     # user = User(username=validated_data['username'])
    #     # # 使用user.set_password()对密码编码，而不使用原始字符作为密码
    #     # user.set_password(validated_data['password'])
    #     # user.save()  # 保存User的实例
    #     # # 保存User实例后，在Token模型（数据库表）中，也对应保存一个Token实例作为用户的token
    #     # token = Token.objects.create(user=user)
    #     # return user
    #     return User.objects.create_user(**validated_data)
