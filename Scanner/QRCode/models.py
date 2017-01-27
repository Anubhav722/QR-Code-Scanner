from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import pre_save
from django.dispatch import receiver
import qrcode
from django.utils.crypto import get_random_string
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from datetime import datetime
# Create your models here.
AUTH_TOKEN_LENGTH = 15

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description =models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    qr_code = models.ImageField(upload_to=upload_location, null=True, blank=True)
    auth_token = models.CharField(max_length=20)

    def __unicode__(self):
        return self.user.username

@receiver(pre_save, sender = UserProfile)
def qr_code_save_call_back(sender, instance, *args, **kwargs):
    if not instance.qr_code:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        instance.auth_token = get_random_string(length=AUTH_TOKEN_LENGTH)
        context = [instance.user.username, instance.auth_token]
        qr.add_data(context)
        qr.make(fit=True)

        img = qr.make_image(fill_color="red", back_color="yellow")
        buffer = StringIO.StringIO()
        img.save(buffer)
        filename = 'events-%s.png' % (instance.user.username)
        filebuffer = InMemoryUploadedFile(
            buffer, None, filename, 'image/png', buffer.len, None)

        instance.qr_code.save(filename, filebuffer)


# Understanding the time module

# import datetime
# from datetime import timedelta
# x=datetime.datetime.now()
# print datetime.datetime.now()
# # add 1 day
# print datetime.datetime.now() + datetime.timedelta(days=1)
#
# # substract 60 seconds
# print datetime.datetime.now() - datetime.timedelta(seconds=60)
#
# #Add 2 years.
# print datetime.datetime.now() + datetime.timedelta(days=730)
#
# print datetime.date.today()
# print x.hour
# print x.minute

# Understanding the timer now # look for threading too i.e. import threading
# import sched, time
# s = sched.scheduler(time.time, time.sleep)
# def do_something(sc):
#     print "Doing stuff..."
#     # do your stuff
#     s.enter(60, 1, do_something, (sc,))
#
# s.enter(60, 1, do_something, (s,))
# s.run()