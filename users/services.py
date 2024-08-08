def set_role(user):
    if user.role == 'admin':
        user.is_staff = True
        user.is_superuser = True
    else:
        user.is_staff = False
        user.is_superuser = False
