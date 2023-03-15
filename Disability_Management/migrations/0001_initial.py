# Generated by Django 4.0.8 on 2023-03-14 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('date', models.CharField(max_length=20)),
                ('picture', models.ImageField(null=True, upload_to='disability/static/images')),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=10)),
                ('telephone', models.CharField(max_length=20)),
                ('nhis', models.CharField(max_length=30)),
                ('type_of_diasbilities', models.CharField(max_length=50, null=True)),
                ('rescidential', models.CharField(max_length=50)),
                ('educational_level', models.CharField(max_length=30)),
                ('school_vocation', models.CharField(max_length=20)),
                ('school', models.CharField(max_length=50)),
                ('guardian_name', models.CharField(max_length=50)),
                ('occupation_g', models.CharField(max_length=30)),
                ('type_of_support', models.CharField(max_length=20)),
                ('disability', models.CharField(max_length=20)),
            ],
        ),
    ]