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

TOKEN_TYPE = 'Bearer'

OBJECTIVE = 1
FEED = 1 << 1
RECOGNITION = 1 << 2
NETWORK_POST = 1 << 3
FEEDBACK = 1 << 4
USERS = 1 << 5
PLACEHOLDER_2 = 1 << 6
PLACEHOLDER_3 = 1 << 7
PLACEHOLDER_4 = 1 << 8
PLACEHOLDER_5 = 1 << 9
PLACEHOLDER_6 = 1 << 10
PLACEHOLDER_7 = 1 << 11
PLACEHOLDER_8 = 1 << 12
PLACEHOLDER_9 = 1 << 13
PLACEHOLDER_10 = 1 << 14
PLACEHOLDER_11 = 1 << 15
PLACEHOLDER_12 = 1 << 16
PLACEHOLDER_13 = 1 << 17
PLACEHOLDER_14 = 1 << 18
PLACEHOLDER_15 = 1 << 19
PLACEHOLDER_16 = 1 << 20
PLACEHOLDER_17 = 1 << 21
PLACEHOLDER_18 = 1 << 22
PLACEHOLDER_19 = 1 << 23
PLACEHOLDER_20 = 1 << 24

ALL = OBJECTIVE | FEED | RECOGNITION | NETWORK_POST | FEEDBACK | USERS | PLACEHOLDER_2 | PLACEHOLDER_3 | PLACEHOLDER_4 | PLACEHOLDER_5 | PLACEHOLDER_6 | PLACEHOLDER_7 | PLACEHOLDER_8 | PLACEHOLDER_9 | PLACEHOLDER_10 | PLACEHOLDER_11 | PLACEHOLDER_12 | PLACEHOLDER_13 | PLACEHOLDER_14 | PLACEHOLDER_15 | PLACEHOLDER_16 | PLACEHOLDER_17 | PLACEHOLDER_18 | PLACEHOLDER_19 | PLACEHOLDER_20

DEFAULT_SCOPES = (
    (USERS, 'user'),
    (OBJECTIVE, 'objective'),
    (FEED, 'feed'),
    (RECOGNITION, 'recognition'),
    (NETWORK_POST, 'network_post'),
    (FEEDBACK, 'feedback'),
    (ALL, 'all'),
)

SCOPES = getattr(settings, 'OAUTH_SCOPES', DEFAULT_SCOPES)

EXPIRE_DELTA = getattr(settings, 'OAUTH_EXPIRE_DELTA', timedelta(days=365))

# Expiry delta for public clients (which typically have shorter lived tokens)
EXPIRE_DELTA_PUBLIC = getattr(settings, 'OAUTH_EXPIRE_DELTA_PUBLIC', timedelta(days=30))

EXPIRE_CODE_DELTA = getattr(settings, 'OAUTH_EXPIRE_CODE_DELTA', timedelta(seconds=10 * 60))

# Remove expired tokens immediately instead of letting them persist.
DELETE_EXPIRED = getattr(settings, 'OAUTH_DELETE_EXPIRED', False)

ENFORCE_SECURE = getattr(settings, 'OAUTH_ENFORCE_SECURE', False)
ENFORCE_CLIENT_SECURE = getattr(settings, 'OAUTH_ENFORCE_CLIENT_SECURE', True)

SESSION_KEY = getattr(settings, 'OAUTH_SESSION_KEY', 'oauth')

SINGLE_ACCESS_TOKEN = getattr(settings, 'OAUTH_SINGLE_ACCESS_TOKEN', False)
