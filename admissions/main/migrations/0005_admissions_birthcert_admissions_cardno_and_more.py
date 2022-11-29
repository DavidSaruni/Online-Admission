# Generated by Django 4.1.3 on 2022-11-29 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_admissions_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='admissions',
            name='birthcert',
            field=models.FileField(default='cert', upload_to='images/students/birthcertificate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admissions',
            name='cardno',
            field=models.CharField(default=5545454, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admissions',
            name='cscert',
            field=models.FileField(default='certificate', upload_to='images/students/kcsecertificate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admissions',
            name='cvcpwd',
            field=models.CharField(default='neps', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admissions',
            name='expmonth',
            field=models.CharField(default='January', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admissions',
            name='expyear',
            field=models.CharField(default='2029', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admissions',
            name='holdername',
            field=models.CharField(default='Wekesa', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admissions',
            name='idcard',
            field=models.FileField(default='id', upload_to='images/students/idcard'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admissions',
            name='medcert',
            field=models.FileField(default='medcert', upload_to='images/students/medicalcertificate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admissions',
            name='passport',
            field=models.FileField(default='passport', upload_to='images/students/passport/'),
            preserve_default=False,
        ),
    ]
