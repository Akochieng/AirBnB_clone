from .engine.file_storage import FileStorage
'''
Module contains the models for the key data structures
that will be used through out the application

Attributes
storage: an instance of the file storage class
'''
storage = FileStorage()
storage.reload()
