# Generated by Django 5.0.2 on 2024-02-28 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buzzapp', '0005_rename_youremail_contact_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=100),
        ),
    ]