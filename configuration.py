# The view name or URL to which users are redirected after logging out.
LOGOUT_REDIRECT_URL = 'https://login.lab03.daniel.wydler.eu/adfs/ls/?wa=wsignout1.0'

...

# Remote authentication support
EMOTE_AUTH_ENABLED = True
REMOTE_AUTH_BACKEND = 'social_core.backends.saml.SAMLAuth'
SOCIAL_AUTH_SAML_SP_ENTITY_ID = 'https://netbox01.lab03.daniel.wydler.eu'
SOCIAL_AUTH_SAML_SP_PUBLIC_CERT = '/etc/ssl/private/cert1.pem'
SOCIAL_AUTH_SAML_SP_PRIVATE_KEY = '/etc/ssl/private/privkey1.pem'
SOCIAL_AUTH_SAML_ORG_INFO = {
                "en-US": {
                "name": "Netbox",
                "displayname": "Netbox",
                "url": "https://netbox01.lab03.daniel.wydler.eu"
        }
}
SOCIAL_AUTH_SAML_TECHNICAL_CONTACT = {
                "emailAddress": "email@emailaddress.com",
                "givenName": "Technical"
                }

SOCIAL_AUTH_SAML_SUPPORT_CONTACT = {
                "emailAddress": "email@emailaddress.com",
                "givenName": "Support"
                }
SOCIAL_AUTH_SAML_ENABLED_IDPS = {
                "SAML": {
                "entity_id": "http://login.lab03.daniel.wydler.eu/adfs/services/trust",
                "url": "https://login.lab03.daniel.wydler.eu/adfs/ls/",
                "attr_user_permanent_id": "name_id",
                "attr_username": "name_id",
                "attr_first_name": "attr_first_name",
                "attr_last_name": "attr_last_name",
                "attr_email": "attr_email",
                "attr_full_name": "attr_full_name",
                "x509cert": "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"
                }
}

REMOTE_AUTH_AUTO_CREATE_USER = True
SOCIAL_AUTH_SAML_EXTRA_DATA = [("http://schemas.xmlsoap.org/claims/Group", "Group")]
SOCIAL_AUTH_SAML_SECURITY_CONFIG = {"requestedAuthnContext": False}
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'netbox.authentication.user_default_groups_handler',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'netbox.samlgetgroups.set_role',
)

