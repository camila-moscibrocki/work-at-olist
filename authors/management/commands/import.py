from django.core.management.base import BaseCommand, CommandError
from authors.models import Author
import csv


class Command(BaseCommand):
    """
    Call authors from a CSV input file
    """
    help = "CSV file for books database"

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='CSV File name')

    def handle(self, *args, **options):
        filename = options['file']
        if not filename:
            raise CommandError('Not filename')
        errors = False
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            try:
                authors = [Author(name=row['name']) for row in reader]
            except KeyError:
                errors = True
        if errors:
            self.stdout.write(self.style.ERROR('Please, insert "name" column in CSV file'))
            return
        created = Author.objects.bulk_create(authors, ignore_conflicts=True)
        count = len(created)
        if not count:
            self.stdout.write(self.style.WARNING('Author not inserted in the base, check registers'))
        self.stdout.write(
            self.style.SUCCESS(
                f'Imported CSV file {count} '
                f'author{"s" if count != 1 else ""}. '
            )
        )