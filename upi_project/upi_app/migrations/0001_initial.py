# Generated by Django 4.1.3 on 2022-11-15 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=20)),
                ('ifsc_code', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=10)),
                ('branch_name', models.CharField(max_length=30)),
                ('mobile_number', models.CharField(max_length=10)),
            ],
        ),
    ]