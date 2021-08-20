# Generated by Django 2.2.6 on 2021-08-16 23:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0008_merge_20210816_1735"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                max_length=256, unique=True, verbose_name="название"
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name="genre",
            name="name",
            field=models.CharField(
                max_length=256, unique=True, verbose_name="название жанра"
            ),
        ),
        migrations.AlterField(
            model_name="title",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="titles",
                to="reviews.Category",
                verbose_name="категория произведения",
            ),
        ),
        migrations.AlterField(
            model_name="title",
            name="description",
            field=models.TextField(
                default="описание не предоставлено",
                max_length=300,
                verbose_name="описание произведения",
            ),
        ),
        migrations.AlterField(
            model_name="title",
            name="genre",
            field=models.ManyToManyField(
                through="reviews.GenreTitle",
                to="reviews.Genre",
                verbose_name="жанр произведения",
            ),
        ),
        migrations.AlterField(
            model_name="title",
            name="name",
            field=models.CharField(
                max_length=256, verbose_name="название произведения"
            ),
        ),
        migrations.AlterField(
            model_name="title",
            name="year",
            field=models.PositiveSmallIntegerField(
                blank=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(2021),
                ],
                verbose_name="год выпуска произведения",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Определяет, следует ли считать этого пользователя активным.",
                verbose_name="активный",
            ),
        ),
    ]