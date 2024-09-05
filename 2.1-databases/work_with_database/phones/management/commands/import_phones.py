import csv
from django.core.management.base import BaseCommand
from phones.models import Phone
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = 'Import phones from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        try:
            with open(csv_file_path, 'r') as file:
                reader = csv.DictReader(file, delimiter=',')  # Change delimiter if needed
                for row in reader:
                    phone, created = Phone.objects.update_or_create(
                        slug=slugify(row.get('name')),
                        defaults={
                            'name': row.get('name'),
                            'image': row.get('image'),
                            'price': row.get('price'),
                            'release_date': row.get('release_date'),
                            'lte_exists': row.get('lte_exists') == 'True'
                        }
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Successfully created phone: {phone.name}'))
                    else:
                        self.stdout.write(self.style.SUCCESS(f'Updated phone: {phone.name}'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File {csv_file_path} not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
