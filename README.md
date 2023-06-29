# netbox-sso-saml

The configuration and files that are needed to create SSO with SAML for AzureAD.

All credits go to billylebegue.

See link:
https://www.reddit.com/r/Netbox/comments/104ouqz/netbox_saml_with_azure_ad_authorization/

## Steps:
## Step 1: Setup SSO azure app
![afbeelding](https://github.com/deku-m/netbox-sso-saml/assets/37069737/4b6aec3f-6f94-438e-b2ac-4dd50bab4b7b)
![afbeelding](https://github.com/deku-m/netbox-sso-saml/assets/37069737/28538485-da5e-4192-baab-df20ca242387)
![afbeelding](https://github.com/deku-m/netbox-sso-saml/assets/37069737/b0d36274-8e14-4c52-8a9c-6d313bfc4bcb)

## Step 2: Add library/modules to local_requirements.txt
Go to location of netbox folder (/opt/netbox/) and add in local_requirements.txt the following modules/library
- python3-saml
- onelogin

## Step 3: Dependancies install (because xmlsec in pip is broken i had luck with these below)
Install the linux dependancies for xmlsec1 
- apt install xmlsec1 xmlsec1-devel xmlsec1-openssl-devel libtool-ltdl-devel libxml2-devel libxmlsec1-dev libxmlsec1-openssl pkg-config

## Step 4: Add code to configuration.py
Go to the location of netbox folder (opt/netbox/netbox/netbox)
Paste the content from configuration.py in file and edit the values to match your setup
- SOCIAL_AUTH_SAML_SP_ENTITY_ID
- SOCIAL_AUTH_SAML_SP_PUBLIC_CERT
- SOCIAL_AUTH_SAML_SP_PRIVATE_KEY
- SOCIAL_AUTH_SAML_TECHNICAL_CONTACT
- SOCIAL_AUTH_SAML_SUPPORT_CONTACT
- SOCIAL_AUTH_SAML_ENABLED_IDPS

## Step 5: Create file samlgetgroup.py
Create the file in the same location as configuration.py, paste the content in the file and save.

## Step 6: Run ./upgrade of update docker
Run the file upgrade.sh (./upgrade.sh) located in /opt/netbox/ or rebuild the docker to get the new modules loaded.

## Step 7: Restart service or reboot
Restart the services (systemctl restart netbox netbox-rq) or do a manual reboot
