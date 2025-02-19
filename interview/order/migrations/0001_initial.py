# Generated by Django 4.1.7 on 2023-03-22 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderTag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                ("start_date", models.DateField()),
                ("embargo_date", models.DateField()),
                (
                    "inventory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to="inventory.inventory",
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(related_name="orders", to="order.ordertag"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
