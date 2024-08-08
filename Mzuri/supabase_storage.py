from django.core.files.storage import Storage
from supabase import create_client, Client

class SupabaseStorage(Storage):
    def __init__(self, *args, **kwargs):
        self.supabase: Client = create_client(
            "https://awyfrizifwpimengjboq.supabase.co", 
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF3eWZyaXppZndwaW1lbmdqYm9xIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjMwMTg2OTksImV4cCI6MjAzODU5NDY5OX0.gGUnm_TkDIiPLUK8ctRa0OE7-xpZXPNbEk1ZQNGzCNo"
        )
        super().__init__(*args, **kwargs)

    def _save(self, name, content):
        bucket = self.supabase.storage.from_("Mzuri_uploads")
        bucket.upload(name, content)
        return name

    def _open(self, name, mode='rb'):
        bucket = self.supabase.storage.from_("Mzuri_uploads")
        file = bucket.download(name)
        return file

    def url(self, name):
        bucket = self.supabase.storage.from_("Mzuri_uploads")
        response = bucket.get_public_url(name)
        if isinstance(response, dict) and 'publicURL' in response:
            return response['publicURL']
        return response

    def exists(self, name):
        bucket = self.supabase.storage.from_("Mzuri_uploads")
        response = bucket.list(prefix=name)
        # Check if any files with the given name exist
        return len(response) > 0
