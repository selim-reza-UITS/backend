from django.db import models
from ckeditor.fields import HTMLField

class PrivacyPolicy(models.Model):
    content = HTMLField()

    class Meta:
        verbose_name_plural = 'Privacy Policy'

    def __str__(self):
        return "Privacy Policy"

class TermsConditions(models.Model):
    content = HTMLField()

    class Meta:
        verbose_name_plural = 'Terms & Conditions'

    def __str__(self):
        return "Terms & Conditions"
