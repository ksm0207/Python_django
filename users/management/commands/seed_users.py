from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):

    help = "안녕하세요 나는 개발자 입니다"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="내 이름은 김성민 입니다",
        )

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number}명 유저 대량 생성 완료"))
