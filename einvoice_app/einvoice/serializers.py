from rest_framework.serializers import ModelSerializer
from einvoice_app.einvoice.models import Hello


class HelloSerializer(ModelSerializer):
    class Meta:
        model = Hello
        fields = "__all__"
