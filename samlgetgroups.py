from django.contrib.auth.models import Group

class AuthFailed(Exception):
        pass

def set_role(response, user, backend, *args, **kwargs):
    try:
        conndetails = user.social_auth.get(provider='saml')
        roles = conndetails.extra_data['Group']
    except KeyError:
        user.groups.clear()
        raise AuthFailed("No role assigned")

    try:
        user.is_superuser = False
        user.is_staff = False

        for role in roles:
            if role == 'administrators':
                user.is_superuser = True
                user.save()
                user.is_staff = True
                user.save()
            else:
                user.is_superuser = False
                user.save()
                user.is_staff = False
                user.save()

        group, created = Group.objects.get_or_create(name=role)
        group.user_set.add(user)
    except Group.DoesNotExist:
        pass

