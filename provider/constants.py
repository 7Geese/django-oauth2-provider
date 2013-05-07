from datetime import timedelta
from django.conf import settings

CONFIDENTIAL = 0
PUBLIC = 1
AUTO_GENERATED = 2

CLIENT_TYPES = (
    (CONFIDENTIAL, "Confidential (Web applications)"),
    (PUBLIC, "Public (Native and JS applications)"),
    (AUTO_GENERATED, "Auto Generated applications by the web app")
)

RESPONSE_TYPE_CHOICES = getattr(settings, 'OAUTH_RESPONSE_TYPE_CHOICES', ("code", "token"))

OBJECTIVE = 1 << 1
FEED = 1 << 2
RECOGNITION = 1 << 3
NETWORK_POST = 1 << 4
FEEDBACK = 1 << 5
ALL = 1 << 32

DEFAULT_SCOPES = (
    (OBJECTIVE, 'objective'),
    (FEED, 'feed'),
    (RECOGNITION, 'recognition'),
    (NETWORK_POST, 'network_post'),
    (FEEDBACK, 'feedback'),
    (ALL, 'all'),
)

SCOPES = getattr(settings, 'OAUTH_SCOPES', DEFAULT_SCOPES)

EXPIRE_DELTA = getattr(settings, 'OAUTH_EXPIRE_DELTA', timedelta(days=365))

EXPIRE_CODE_DELTA = getattr(settings, 'OAUTH_EXPIRE_CODE_DELTA', timedelta(seconds=10 * 60))

ENFORCE_SECURE = getattr(settings, 'OAUTH_ENFORCE_SECURE', False)
ENFORCE_CLIENT_SECURE = getattr(settings, 'OAUTH_ENFORCE_CLIENT_SECURE', True)

SESSION_KEY = getattr(settings, 'OAUTH_SESSION_KEY', 'oauth')
