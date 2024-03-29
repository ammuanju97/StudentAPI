# Generated by Django 3.2.12 on 2022-03-08 06:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMarkDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_mark', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('maths_mark', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('science_mark', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('malayalam_mark', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('total_mark', models.DecimalField(blank=True, decimal_places=2, default=100.0, max_digits=3, null=True)),
                ('grand_total', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('grade', models.CharField(blank=True, choices=[('90-100', 'A+'), ('80-89', 'A'), ('70-79', 'B+'), ('50-69', 'B'), ('40-50', 'P'), ('0-39', 'F')], default='F', max_length=10, null=True)),
                ('final_result', models.CharField(blank=True, choices=[('Outstanding', 'Outstanding'), ('Distinction', 'Distinction'), ('Pass', 'Pass'), ('Fail', 'Fail')], default='Fail', max_length=15, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
