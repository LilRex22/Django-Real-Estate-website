from django.contrib.auth.tokens import PasswordResetTokenGenerator

class EmailVerificationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, obj, timestamp):
        return f"{obj.pk}{obj.email}{obj.verified}"

email_verification_token = EmailVerificationTokenGenerator()