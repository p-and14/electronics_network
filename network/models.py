from django.db import models


class Address(models.Model):
    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    country = models.CharField(verbose_name="Страна", max_length=30)
    city = models.CharField(verbose_name="Город", max_length=30)
    street = models.CharField(verbose_name="Улица", max_length=50)
    house_number = models.PositiveSmallIntegerField(verbose_name="Номер дома")

    def __str__(self):
        return f"{self.country}, {self.city}, ул. {self.street}, д.{self.house_number}"


class Contact(models.Model):
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    email = models.EmailField(verbose_name="Почта")
    address = models.ForeignKey(
        Address,
        verbose_name="Адрес",
        on_delete=models.CASCADE,
        related_name="contact"
    )

    def __str__(self):
        return self.email


class Product(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    title = models.CharField(verbose_name="Название", max_length=30)
    model = models.CharField(verbose_name="Модель", max_length=30)
    launch_date = models.DateField(verbose_name="Дата выхода на рынок")

    def __str__(self):
        return self.title


class Organization(models.Model):
    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    class Level(models.IntegerChoices):
        factory = 1, "Завод"
        distributor = 2, "Дистрибьютор"
        dealership = 3, "Дилерский центр"
        large_retail_network = 4, "Крупная розничная сеть"
        individual_entrepreneur = 5, "Индивидуальный предприниматель"

    title = models.CharField(verbose_name="Название", max_length=30)
    level = models.PositiveSmallIntegerField(
        verbose_name="Уровень",
        choices=Level.choices,
    )
    contacts = models.ForeignKey(
        Contact,
        verbose_name="Контакты",
        on_delete=models.CASCADE,
        related_name="organization",
        null=True,
        blank=True
    )
    products = models.ManyToManyField(
        Product,
        verbose_name="Продукты",
        related_name="organizations",
        blank=True
    )
    staff = models.ManyToManyField(
        "staff.Employee",
        verbose_name="Сотрудники",
        related_name="organization",
        blank=True
    )
    supplier = models.ForeignKey(
        "Organization",
        verbose_name="Поставщик",
        on_delete=models.PROTECT,
        related_name="client",
        null=True,
        blank=True
    )
    debt_to_supplier = models.DecimalField(
        verbose_name="Задолженность (руб.)",
        max_digits=15,
        decimal_places=2,
        default=0.00
    )
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    def __str__(self):
        return self.title
