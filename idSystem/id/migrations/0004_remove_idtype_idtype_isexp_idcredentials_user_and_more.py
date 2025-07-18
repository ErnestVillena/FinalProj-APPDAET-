# Generated by Django 5.2.4 on 2025-07-16 02:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('id', '0003_idtype_idtype_expdate_idtype_idtype_issauth_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idtype',
            name='idType_isexp',
        ),
        migrations.AddField(
            model_name='idcredentials',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='idtype',
            name='idType_verify_stat',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Verified', 'Verfied'), ('Rejected', 'Rejected')], default='Pending', max_length=10),
        ),
        migrations.AddField(
            model_name='idtype',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='idtype',
            name='idType_image',
            field=models.ImageField(default='default.png', upload_to='id_image/'),
        ),
        migrations.CreateModel(
            name='IdAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', upload_to='id_attachments/')),
                ('id_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='id.idtype')),
            ],
        ),
    ]
