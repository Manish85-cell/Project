# Generated by Django 4.1.7 on 2024-07-07 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oj', '0002_problems'),
    ]

    operations = [
        migrations.AddField(
            model_name='problems',
            name='examples',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.CreateModel(
            name='Testcase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_data', models.TextField()),
                ('output_data', models.TextField()),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_cases', to='oj.problems')),
            ],
        ),
    ]
