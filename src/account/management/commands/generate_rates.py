import random

from django.core.management.base import BaseCommand

from rate.models import Rate
from rate import model_choices as mch


class Command(BaseCommand):
    help = 'Generate random students'  # noqa  help is python builtins but django command requires it.

    def handle(self, *args, **options):
        for _ in range(10_000):
            Rate.objects.create(
                amount=random.randint(20, 30),
                source=random.choice(mch.SOURCE_CHOICES)[0],
                currency_type=random.choice(mch.CURRENCY_TYPE_CHOICES)[0],
                type=random.choice(mch.RATE_TYPE_CHOICES)[0],

            )
