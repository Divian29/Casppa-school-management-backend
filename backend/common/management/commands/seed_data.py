from django.core.management.base import BaseCommand

from schools.models import School, SchoolClass, House
from parents.models import Parent


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        school, _ = School.objects.get_or_create(
            name="CASPPA School"
        )

        SchoolClass.objects.get_or_create(
            name="Primary 1",
            school=school
        )

        House.objects.get_or_create(
            name="Red",
            school=school
        )

        Parent.objects.get_or_create(
            first_name="John",
            last_name="Doe",
            email="john@example.com"
        )


        self.stdout.write(
            self.style.SUCCESS(
                "Seed data created"
            )
        )