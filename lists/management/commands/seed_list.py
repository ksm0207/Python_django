import random

from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists import models as list_models
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):

    help = "안녕하세요 나는 개발자 입니다"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="내 이름은 김성민 입니다",
        )

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(
            list_models.List, number, {"user": lambda x: random.choice(users)},
        )
        created = seeder.execute()
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
            list_model = list_models.List.objects.get(pk=pk)
            to_add = rooms[random.randint(0, 5) : random.randint(6, 30)]
            list_model.rooms.add(*to_add)

        self.stdout.write(self.style.SUCCESS(f"{number}명 리스트 대량 생성 완료"))
