from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Foydalanuvchilarda telefon raqami mavjud bo\'lishi shart')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        user = self.create_user(phone_number=phone_number, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.role = 'admin'
        user.save(using=self._db)
        return user

    def create_teacher(self, phone_number, password=None, **extra_fields):
        user = self.create_user(phone_number=phone_number, password=password, **extra_fields)
        user.role = 'teacher'
        user.save(using=self._db)
        return user
