# Generated by Django 4.1.5 on 2023-01-30 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("shop", "0001_initial"),
        ("cart", "0002_remove_cart_item_cart_remove_cart_item_product_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
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
                ("cart_id", models.CharField(blank=True, max_length=250)),
                ("date_added", models.DateField(auto_now_add=True)),
            ],
            options={
                "db_table": "Cart",
                "ordering": ["date_added"],
            },
        ),
        migrations.CreateModel(
            name="Cart_item",
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
                ("quantity", models.IntegerField()),
                ("active", models.BooleanField(default=True)),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cart.cart"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.product"
                    ),
                ),
            ],
            options={
                "db_table": "Cart_item",
            },
        ),
    ]