from django.db import models
from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from urlparse import urlparse
from django.conf import settings
import requests

FP_FILE_DOMAINS = getattr(settings, 'FP_FILE_DOMAINS', ['filepicker.io'])

class FilePickerURLField(models.FileField):
    """
    Acts like a URLField that will download any filepicker.io file it sees, 
    upload the file to the media storage, replacing the filepicker.io URL with
    the one for the storage.    
    """

    _errors = {
        'failed': _('failed to download file'),
    }

    def pre_save(self, instance, creating):
        """
        Check for a FilePicker.io URL and upload it to storage.
        """

        value = getattr(instance, self.attname)

        if not self._is_filepicker_file(value):
            return value

        return self.storage.save(self.upload_to(value), self._download_file(value))

    def _is_filepicker_file(self, url):
        """
        Tests the URL to see if it's a filepicker URL
        """
        parsed = urlparse(url)
        return parsed.netloc in FP_FILE_DOMAINS

    def _download_file(self, url):
        """
        Downloads the file at the given URL
        """

        req = requests.get(url)

        if req.status_code != 200:
            raise ValidationError(self._errors['failed'])

        return ContentFile(req.content)