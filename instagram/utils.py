# -*- coding: utf-8 -*-

from django.utils.deconstruct import deconstructible


@deconstructible
class FilePathManager(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def _gen_filename_hash(self):
        import uuid
        return str(uuid.uuid4())

    def __call__(self, instance, filename):
        import time
        import datetime
        import os
        name, extend = os.path.splitext(filename)
        name = self._gen_filename_hash()
        filename = "%s%s" % (name, extend)
        return self.path + str(datetime.datetime.now().strftime("%Y%m%d")) + "/" + filename

