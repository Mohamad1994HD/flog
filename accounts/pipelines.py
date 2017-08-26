from requests import request, HTTPError

from django.core.files.base import ContentFile

def grab_profile_pic(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        if backend.name == 'facebook':
            url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])

            try:
                response = request('GET', url, params={'type': 'large'})
                response.raise_for_status()
            except HTTPError:
                pass
            else:
                profile = user.profile
                profile.image.save('{0}_social.jpg'.format(user.username),
                                   ContentFile(response.content))
                profile.save()


