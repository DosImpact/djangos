# Generated by Django 2.2.6 on 2019-10-09 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opencvwebapp', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUploadModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='images/%Y/%m/%d')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]