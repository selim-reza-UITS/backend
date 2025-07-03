from rest_framework import serializers
from app.admin.models import PrivacyPolicy, TermsConditions

class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = ['content']

class TermsConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermsConditions
        fields = ['content']
