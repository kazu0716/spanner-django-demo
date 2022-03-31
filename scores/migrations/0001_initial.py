# Generated by Django 3.2.6 on 2022-03-31 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('score_id', models.UUIDField(default='f2a104e32c71436ebae9412f7cb55ee4', editable=False, primary_key=True, serialize=False)),
                ('user_id', models.UUIDField()),
                ('score', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Scores',
            },
        ),
    ]
