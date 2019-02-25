# Generated by Django 2.1.5 on 2019-02-24 00:11

from django.db import migrations, models
import django.db.models.deletion
import yaris.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Giden',
                'verbose_name_plural': 'Gidenler',
            },
        ),
        migrations.CreateModel(
            name='iller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('il', models.CharField(max_length=255, unique=True, verbose_name='İl adi')),
                ('slug', models.SlugField()),
                ('kayit', models.DateTimeField(auto_now_add=True)),
                ('guncelleme', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'il',
                'verbose_name_plural': 'İller',
            },
        ),
        migrations.CreateModel(
            name='katilimci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=120, verbose_name='Takma isim')),
                ('name', models.CharField(blank=True, max_length=60, verbose_name='Adı')),
                ('lastname', models.CharField(blank=True, max_length=60, verbose_name='Soyadı')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-posta')),
                ('mobile', models.CharField(blank=True, max_length=20, verbose_name='Cep Telefonu')),
                ('kayit', models.DateTimeField(auto_now_add=True)),
                ('il', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yaris.iller', verbose_name='İl')),
            ],
            options={
                'verbose_name': 'Katılımcı',
                'verbose_name_plural': 'Katılımcılar',
            },
        ),
        migrations.CreateModel(
            name='kurallar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kural', models.IntegerField()),
                ('aciklama', models.TextField()),
            ],
            options={
                'verbose_name': 'Kural',
                'verbose_name_plural': 'Kurallar',
            },
        ),
        migrations.CreateModel(
            name='oduller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, verbose_name='Başlık')),
                ('sira', models.IntegerField(verbose_name='Sıra')),
                ('odul', models.CharField(max_length=120, verbose_name='Ödül')),
            ],
            options={
                'verbose_name': 'oduller',
                'verbose_name_plural': 'oduller',
            },
        ),
        migrations.CreateModel(
            name='Pigeon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yil', models.DateField(verbose_name='Yıl')),
                ('kunye', models.CharField(max_length=30, verbose_name='Künye')),
                ('ucret', models.IntegerField(default=0, verbose_name='Alıncan Ücret')),
                ('kayit', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Kuş',
                'verbose_name_plural': 'Kuşları',
            },
        ),
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('sira', models.IntegerField()),
                ('puan', models.IntegerField()),
                ('kus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yaris.Pigeon')),
            ],
            options={
                'verbose_name': 'Sonuc',
                'verbose_name_plural': 'Sonuçlar',
            },
        ),
        migrations.CreateModel(
            name='sezon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Başlık')),
                ('start_date', models.DateField(verbose_name='Başlangıc Tarihi')),
                ('end_date', models.DateField(verbose_name='Bitiş Tarihi')),
            ],
            options={
                'verbose_name': 'Sezon',
                'verbose_name_plural': 'Sezonlar',
            },
        ),
        migrations.CreateModel(
            name='sponsorlar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsor', models.CharField(max_length=120, verbose_name='Sponsor')),
                ('logo', models.ImageField(upload_to=yaris.models.logos)),
            ],
            options={
                'verbose_name': 'Sponsor',
                'verbose_name_plural': 'Sponsorlar',
            },
        ),
        migrations.CreateModel(
            name='temsilci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adi', models.CharField(max_length=60, verbose_name='Adı')),
                ('soyadi', models.CharField(max_length=60, verbose_name='Soyadı')),
                ('eposta', models.CharField(blank=True, max_length=120, verbose_name='E-posta')),
                ('mobil', models.CharField(blank=True, max_length=25, verbose_name='Cep Telefonu')),
                ('facebook', models.CharField(blank=True, max_length=150, verbose_name='Facebook Adresi')),
                ('il', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yaris.iller', verbose_name='İl')),
            ],
            options={
                'verbose_name': 'Temsilci',
                'verbose_name_plural': 'Temsilciler',
            },
        ),
        migrations.CreateModel(
            name='ulkeler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ulke', models.CharField(max_length=200, unique=True, verbose_name='Ülke')),
                ('kod', models.CharField(blank=True, help_text='TR', max_length=3, null=True, verbose_name='Ülke Kodu')),
                ('slug', models.SlugField()),
                ('kayit', models.DateTimeField(auto_now_add=True)),
                ('guncelleme', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Ülke',
                'verbose_name_plural': 'Ülkeler',
            },
        ),
        migrations.CreateModel(
            name='yaris',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adi', models.CharField(max_length=120, verbose_name='Adı')),
                ('tarih', models.DateTimeField(verbose_name='Salım Tarihi')),
                ('mesafe', models.IntegerField(verbose_name='Mesafe')),
                ('tip', models.CharField(blank=True, choices=[('1', 'Yarış'), ('2', 'Antrenman')], max_length=2)),
                ('lat', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Enlem')),
                ('lng', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Boylam')),
                ('sicaklik', models.IntegerField(blank=True, null=True, verbose_name='Sıcaklık')),
                ('h_durum', models.CharField(blank=True, max_length=50, null=True, verbose_name='Hava Durumu')),
                ('ruzgar', models.IntegerField(blank=True, null=True, verbose_name='Rüzgar Hızı')),
                ('r_yon', models.CharField(blank=True, max_length=50, null=True, verbose_name='Rüzgar Yönü')),
                ('nem', models.IntegerField(blank=True, null=True, verbose_name='Nem Oranı')),
                ('slug', models.SlugField()),
                ('kayit', models.DateTimeField(auto_now_add=True)),
                ('guncelleme', models.DateTimeField(auto_now=True)),
                ('sezon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yaris.sezon', verbose_name='sezon')),
            ],
            options={
                'verbose_name': 'Yarış',
                'verbose_name_plural': 'Yarışlar',
            },
        ),
        migrations.AddField(
            model_name='temsilci',
            name='ulke',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yaris.ulkeler', verbose_name='Ülke'),
        ),
        migrations.AddField(
            model_name='result',
            name='yaris',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yaris.yaris'),
        ),
        migrations.AddField(
            model_name='pigeon',
            name='ulke',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yaris.ulkeler', verbose_name='Ülke'),
        ),
        migrations.AddField(
            model_name='pigeon',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fanchers', to='yaris.katilimci', verbose_name='Katılımcı'),
        ),
        migrations.AddField(
            model_name='oduller',
            name='yaris',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='yaris.yaris', verbose_name='Yarış'),
        ),
        migrations.AddField(
            model_name='katilimci',
            name='sezon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='katilimcilar', to='yaris.sezon', verbose_name='Sezon'),
        ),
        migrations.AddField(
            model_name='iller',
            name='ulke',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iller', to='yaris.ulkeler', verbose_name='Ülke'),
        ),
        migrations.AddField(
            model_name='basket',
            name='kus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yaris.Pigeon'),
        ),
        migrations.AddField(
            model_name='basket',
            name='yaris',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yaris.yaris'),
        ),
    ]
