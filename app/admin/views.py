from rest_framework import generics
from .models import PrivacyPolicy, TermsConditions
from app.admin.serializers.terms_and_policy import PrivacyPolicySerializer, TermsConditionsSerializer

class PrivacyPolicyView(generics.RetrieveAPIView):
    queryset = PrivacyPolicy.objects.all()
    serializer_class = PrivacyPolicySerializer

    def get_object(self):
        return PrivacyPolicy.objects.first()

class TermsConditionsView(generics.RetrieveAPIView):
    queryset = TermsConditions.objects.all()
    serializer_class = TermsConditionsSerializer

    def get_object(self):
        return TermsConditions.objects.first()
