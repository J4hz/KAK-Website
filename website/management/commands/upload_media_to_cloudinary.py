"""
Management command: upload_media_to_cloudinary

Reads every ImageField value stored in the database, finds the matching
local file under MEDIA_ROOT, uploads it to Cloudinary, and updates the
database record so the field now stores the Cloudinary public_id.

Run ONCE after adding Cloudinary credentials to .env:
    python manage.py upload_media_to_cloudinary
"""

import os
from pathlib import Path
from django.core.management.base import BaseCommand
from django.conf import settings
import cloudinary
import cloudinary.uploader


class Command(BaseCommand):
    help = 'Upload all existing local media files to Cloudinary and update DB records'

    def handle(self, *args, **options):
        cloud_name = settings.CLOUDINARY_STORAGE.get('CLOUD_NAME', '')
        if not cloud_name:
            self.stderr.write('CLOUDINARY_CLOUD_NAME is not set in .env — aborting.')
            return

        cloudinary.config(
            cloud_name=cloud_name,
            api_key=settings.CLOUDINARY_STORAGE['API_KEY'],
            api_secret=settings.CLOUDINARY_STORAGE['API_SECRET'],
        )

        media_root = Path(settings.BASE_DIR) / 'media'

        from website.models import SiteSettings, HeroSection, GalleryImage, TeamMember, Testimonial, NewsPost

        jobs = [
            (SiteSettings, 'logo'),
            (HeroSection, 'background_image'),
            (GalleryImage, 'image'),
            (TeamMember, 'photo'),
            (Testimonial, 'photo'),
            (NewsPost, 'image'),
        ]

        total = 0
        for Model, field_name in jobs:
            for obj in Model.objects.all():
                field = getattr(obj, field_name)
                if not field or not field.name:
                    continue

                local_path = media_root / field.name
                if not local_path.exists():
                    # Cloudinary strips extensions; try common image extensions
                    found = None
                    for ext in ('.jpg', '.jpeg', '.png', '.webp', '.gif'):
                        candidate = media_root / (field.name + ext)
                        if candidate.exists():
                            found = candidate
                            break
                    if not found:
                        self.stdout.write(f'  SKIP (not found locally): {field.name}')
                        continue
                    local_path = found

                # Strip leading media/ from the path to use as public_id folder
                folder = str(Path(field.name).parent).replace('\\', '/')

                self.stdout.write(f'  Uploading {field.name} ...', ending='')
                try:
                    result = cloudinary.uploader.upload(
                        str(local_path),
                        folder=folder,
                        use_filename=True,
                        unique_filename=False,
                        overwrite=True,
                        resource_type='image',
                    )
                    # Cloudinary public_id includes the folder, e.g. "gallery/img001"
                    new_name = result['public_id']
                    # django-cloudinary-storage expects just the public_id as the field value
                    field.name = new_name
                    obj.save(update_fields=[field_name])
                    self.stdout.write(f' OK -> {new_name}')
                    total += 1
                except Exception as e:
                    self.stdout.write(f' ERROR: {e}')

        self.stdout.write(self.style.SUCCESS(f'\nDone. {total} files uploaded to Cloudinary.'))
