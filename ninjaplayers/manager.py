from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, name, grade, ability, password=None):
        if not name:
            raise ValueError('캐릭터 이름을 입력하세요.')
        if not password:
            raise ValueError('비밀번호를 입력하세요.')

        user = self.model(
            name=name,
            grade=grade,
            ability=ability,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, grade, ability, password=None):
        user = self.create_user(
            name=name,
            grade=grade,
            ability=ability,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
