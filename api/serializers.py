import base64
import uuid

from rest_framework import serializers
from django.core.files.base import ContentFile

from contact.models import Contact


class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        if isinstance(data, basestring) and data.startswith('data:image'):
            # base64 encoded image - decode
            format, imgstr = data.split(';base64,')  # format ~= data:image/X,
            ext = format.split('/')[-1]  # guess file extension

            file_name = str(uuid.uuid4())[:12]  # 12 characters
            file_name = "%s.%s" % (file_name, ext)

            data = ContentFile(base64.b64decode(imgstr), name=file_name)

        return super(Base64ImageField, self).to_internal_value(data)


class ContactSerializer(serializers.ModelSerializer):

    """
    Contact serializers
    """

    photo = Base64ImageField(
        source='profile_photo', required=False)

    class Meta:
        model = Contact
        fields = (
            'id', 'first_name', 'last_name', 'company', 'phone_mobile',
            'phone_work', 'phone_home', 'photo', 'address',
            'city', 'state', 'country', 'postal_zip', 'email',
            'website', 'note', 'ip')
