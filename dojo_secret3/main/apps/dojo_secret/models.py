from __future__ import unicode_literals
from django.db import models

from ..login.models import User
# Create your models here.


class SecretManager(models.Manager):
    def make_secret(self, postData, user):
        results = {'create':True, 'errors':[], 'content':None}
        if postData['secret'] == '':
            results['create'] = False
            results['errors'].append('shhhhh we will keep your secret quite, but we need something to post')
        elif results['create']:
            post = postData['secret']
            bunny = Secret.objects.create(content = post, user_id = user)
            bunny.save()
            results['content'] = bunny
        return results

    def make_delete(self, user, temp):
        delete_it = Secret.objects.filter(user_id=user).filter(id=temp).delete()
        return delete_it


class LikeManager(models.Manager):
    def make_like(self, user, temp):
        if len(Like.objects.filter(user_id=user).filter(secret_id=temp)) >0:
            print Like.objects.filter(user_id=user).filter(secret_id=temp)
            print 'no'
            return None
        else:
            like = Like.objects.create(user_id = user, secret_id = temp)
            print 'yes'
            return like

    def make_unlike(self, user, temp):
        unlike = Like.objects.filter(user_id=user).filter(secret_id=temp).delete()
        return unlike



class Secret(models.Model):
    content = models.CharField(max_length = 1000)
    user = models.ForeignKey(User)
    objects = SecretManager()
    def get_like_users(self):
        likes = Like.objects.filter(secret_id=self.id)

        user = []
        for like in likes:
            user.append(like.user_id)
        return user
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Like(models.Model):
    secret = models.ForeignKey(Secret, related_name = 'sec')
    user = models.ForeignKey(User)
    objects = LikeManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
