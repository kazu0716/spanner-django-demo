# Generated by Django 3.2.6 on 2022-03-31 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default='3f937c58c5934ee2b4cab4f6f501b7f6', editable=False, primary_key=True, serialize=False),
        ),
    ]
