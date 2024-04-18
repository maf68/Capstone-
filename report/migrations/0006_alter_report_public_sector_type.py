# Generated by Django 4.1.7 on 2024-04-16 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_alter_report_public_sector_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='public_sector_type',
            field=models.CharField(choices=[('hospitals', 'مستشفيات'), ('ministries', 'وزارات'), ('institutions', 'مؤسسات'), ('banks', 'بنوك'), ('prisons', 'سجون'), ('courts', 'محاكم'), ('universities', 'جامعات'), ('security_institutions', 'مؤسسات امنية')], default='', max_length=100),
        ),
    ]
