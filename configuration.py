# Remote authentication support
REMOTE_AUTH_ENABLED = True
REMOTE_AUTH_BACKEND = 'social_core.backends.saml.SAMLAuth'
SOCIAL_AUTH_SAML_SP_ENTITY_ID = 'https://netbox.example.local'
SOCIAL_AUTH_SAML_SP_PUBLIC_CERT = 'binary-certificate-netbox-see.crt-file'
SOCIAL_AUTH_SAML_SP_PRIVATE_KEY = 'binary-key-certificate-netbox-see-.key-file'
SOCIAL_AUTH_SAML_ORG_INFO = {
                "en-US": {
               "name": "Netbox",
                "displayname": "Netbox",
                "url": "https://netbox.example.local"
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
                "entity_id": "https://sts.windows.net/id-app-on-azure/",
                "url": "https://login.microsoftonline.com/id-app-on-azure/saml2",
                "attr_user_permanent_id": "name_id",
                "attr_username": "name_id",
                "attr_first_name": "attr_first_name",
                "attr_last_name": "attr_last_name",
                "attr_email": "attr_email",
                "attr_full_name": "attr_full_name",
                "x509cert": "app-certificate-on-azure-"
                }
}
REMOTE_AUTH_AUTO_CREATE_USER = True
SOCIAL_AUTH_SAML_EXTRA_DATA = [("http://schemas.microsoft.com/ws/2008/06/identity/claims/groups", "groups")]
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


