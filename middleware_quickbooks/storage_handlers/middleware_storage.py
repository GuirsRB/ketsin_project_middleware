from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os


class MiddlewareStorage(FileSystemStorage):
    def __init__(self):
        super().__init__(str(settings.BASE_DIR.absolute()) + f"{os.sep}files{os.sep}", None, 0o644, None)
