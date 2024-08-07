# Generated by Django 4.1.7 on 2024-07-07 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(choices=[(True, 'Solved'), (False, 'Unsolved')], default=False)),
                ('name', models.CharField(max_length=64)),
                ('statement', models.CharField(max_length=1000)),
                ('constraints', models.CharField(max_length=255)),
                ('difficulty_levels', models.CharField(choices=[('e', 'Easy'), ('m', 'Medium'), ('h', 'hard')], default='easy', max_length=6)),
            ],
        ),
    ]
