import uuid


# Slug Generators
def get_user_slug(instance):
    return f"{instance.first_name}-{instance.last_name}-{str(instance.alias).split('-')[0]}"