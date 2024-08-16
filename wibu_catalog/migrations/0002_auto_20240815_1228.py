# Generated by Django 3.2.12 on 2024-08-15 05:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wibu_catalog', '0001_initial'),
    ]

    operations = [
        # migrations.CreateModel(
        #     name='FavoriteList',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('status', models.CharField(choices=[(1, 'Watching'), (2, 'Completed'), (3, 'On_Hold'), (4, 'Dropped'), (5, 'Re_Watching'), (6, 'Plan_to_Watch')], default='1', help_text='User status with this content.', max_length=1, null=True)),
        #         ('progress', models.IntegerField(default='0', help_text="User's progress (e.g. chapter01).", null=True)),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='ScoreList',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('score', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default='10', help_text="User's score of this content.", null=True)),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='Users',
        #     fields=[
        #         ('uid', models.IntegerField(help_text='User id', primary_key=True, serialize=False)),
        #         ('username', models.CharField(help_text='Username', max_length=255, null=True)),
        #         ('role', models.CharField(choices=[('admin', 'admin'), ('new_user', 'new_user'), ('longtime_user', 'longtime_user'), ('user', 'user'), ('VIP', 'VIP')], default='new_user', help_text='User role.', max_length=20, null=True)),
        #         ('email', models.CharField(help_text='Email address', max_length=255, null=True)),
        #         ('password', models.CharField(help_text='Password', max_length=255, null=True)),
        #         ('dateOfBirth', models.DateField(blank=True, help_text='Date of birth', null=True)),
        #         ('profilePicture', models.ImageField(blank=True, help_text='Profile picture', null=True, upload_to='')),
        #         ('registrationDate', models.DateField(help_text="Account's registration date", null=True)),
        #     ],
        # ),
    #     migrations.AlterUniqueTogether(
    #         name='score_list',
    #         unique_together=None,
    #     ),
    #     migrations.RemoveField(
    #         model_name='score_list',
    #         name='CID',
    #     ),
    #     migrations.RemoveField(
    #         model_name='score_list',
    #         name='UID',
    #     ),
    #     migrations.RenameField(
    #         model_name='comments',
    #         old_name='CID',
    #         new_name='cid',
    #     ),
    #     migrations.RenameField(
    #         model_name='content',
    #         old_name='CID',
    #         new_name='cid',
    #     ),
    #     migrations.RenameField(
    #         model_name='feedback',
    #         old_name='PID',
    #         new_name='pid',
    #     ),
    #     migrations.RenameField(
    #         model_name='notifications',
    #         old_name='Notification_id',
    #         new_name='notificationId',
    #     ),
    #     migrations.RenameField(
    #         model_name='order',
    #         old_name='OID',
    #         new_name='oid',
    #     ),
    #     migrations.RenameField(
    #         model_name='orderitems',
    #         old_name='OID',
    #         new_name='oid',
    #     ),
    #     migrations.RenameField(
    #         model_name='orderitems',
    #         old_name='PID',
    #         new_name='pid',
    #     ),
    #     migrations.RenameField(
    #         model_name='product',
    #         old_name='CID',
    #         new_name='cid',
    #     ),
    #     migrations.RenameField(
    #         model_name='product',
    #         old_name='PID',
    #         new_name='pid',
    #     ),
    #     migrations.RenameField(
    #         model_name='score',
    #         old_name='CID',
    #         new_name='cid',
    #     ),
    #     migrations.RemoveField(
    #         model_name='comments',
    #         name='Content',
    #     ),
    #     migrations.RemoveField(
    #         model_name='comments',
    #         name='Date_of_cmt',
    #     ),
    #     migrations.RemoveField(
    #         model_name='comments',
    #         name='Likes',
    #     ),
    #     migrations.RemoveField(
    #         model_name='comments',
    #         name='UID',
    #     ),
    #     migrations.RemoveField(
    #         model_name='content',
    #         name='Aired',
    #     ),
    #     migrations.RemoveField(
    #         model_name='content',
    #         name='Category',
    #     ),
    #     migrations.RemoveField(
    #         model_name='content',
    #         name='Completed',
    #     ),
    #     migrations.RemoveField(
    #         model_name='content',
    #         name='Ctype',
    #     ),
    #     migrations.RemoveField(
    #         model_name='content',
    #         name='Dropped',
    #     ),
    #     migrations.RemoveField(
    #         model_name='content',
    #         name='Duration',
    #     ),
    #     migrations.RemoveField(
    #         model_name='content',
    #         name='Episodes',
    #     ),
    #     migrations.RemoveField(
    #         model_name='content',
    #         name='Favorites',
    #     ),
    #     migrations.RemoveField(
    #         model_name='content',
    #         name='Genres',
    #     ),
    #     migrations.RemoveField(
    #         model_name='content',
    #         name='Last_update',
    #     ),
    #     migrations.RemoveField(
    #         model_name='content',
    #         name='Licensors',
    #     ),
    #     migrations.RemoveField(
    #         model_name='content',
    #         name='Name',
    #     ),
    #     migrations.RemoveField(
    #         model_name='content',
    #         name='On_Hold',
    #     ),
    #     migrations.RemoveField(
    #         model_name='content',
    #         name='Picture',
    #     ),
    #     migrations.RemoveField(
    #         model_name='content',
    #         name='Plan_to_Watch',
    #     ),
    #     migrations.RemoveField(
    #         model_name='content',
    #         name='Producers',
    #     ),
    #     migrations.RemoveField(
    #         model_name='content',
    #         name='Ranked',
    #     ),
    #     migrations.RemoveField(
    #         model_name='content',
    #         name='Rating',
    #     ),
    #     migrations.RemoveField(
    #         model_name='content',
    #         name='Score_avg',
    #     ),
    #     migrations.RemoveField(
    #         model_name='content',
    #         name='Source',
    #     ),
    #     migrations.RemoveField(
    #         model_name='content',
    #         name='Studios',
    #     ),
    #     migrations.RemoveField(
    #         model_name='content',
    #         name='Watching',
    #     ),
    #     migrations.RemoveField(
    #         model_name='feedback',
    #         name='Cmt',
    #     ),
    #     migrations.RemoveField(
    #         model_name='feedback',
    #         name='Rate',
    #     ),
    #     migrations.RemoveField(
    #         model_name='feedback',
    #         name='UID',
    #     ),
    #     migrations.RemoveField(
    #         model_name='notifications',
    #         name='Date',
    #     ),
    #     migrations.RemoveField(
    #         model_name='notifications',
    #         name='Is_read',
    #     ),
    #     migrations.RemoveField(
    #         model_name='notifications',
    #         name='Message',
    #     ),
    #     migrations.RemoveField(
    #         model_name='notifications',
    #         name='Ntype',
    #     ),
    #     migrations.RemoveField(
    #         model_name='notifications',
    #         name='UID',
    #     ),
    #     migrations.RemoveField(
    #         model_name='order',
    #         name='Order_date',
    #     ),
    #     migrations.RemoveField(
    #         model_name='order',
    #         name='Status',
    #     ),
    #     migrations.RemoveField(
    #         model_name='order',
    #         name='UID',
    #     ),
    #     migrations.RemoveField(
    #         model_name='orderitems',
    #         name='Buy_price',
    #     ),
    #     migrations.RemoveField(
    #         model_name='orderitems',
    #         name='Quantity',
    #     ),
    #     migrations.RemoveField(
    #         model_name='product',
    #         name='Description',
    #     ),
    #     migrations.RemoveField(
    #         model_name='product',
    #         name='Name',
    #     ),
    #     migrations.RemoveField(
    #         model_name='product',
    #         name='Picture',
    #     ),
    #     migrations.RemoveField(
    #         model_name='product',
    #         name='Price',
    #     ),
    #     migrations.RemoveField(
    #         model_name='product',
    #         name='Ravg',
    #     ),
    #     migrations.RemoveField(
    #         model_name='score',
    #         name='Score_1',
    #     ),
    #     migrations.RemoveField(
    #         model_name='score',
    #         name='Score_10',
    #     ),
    #     migrations.RemoveField(
    #         model_name='score',
    #         name='Score_2',
    #     ),
    #     migrations.RemoveField(
    #         model_name='score',
    #         name='Score_3',
    #     ),
    #     migrations.RemoveField(
    #         model_name='score',
    #         name='Score_4',
    #     ),
    #     migrations.RemoveField(
    #         model_name='score',
    #         name='Score_5',
    #     ),
    #     migrations.RemoveField(
    #         model_name='score',
    #         name='Score_6',
    #     ),
    #     migrations.RemoveField(
    #         model_name='score',
    #         name='Score_7',
    #     ),
    #     migrations.RemoveField(
    #         model_name='score',
    #         name='Score_8',
    #     ),
    #     migrations.RemoveField(
    #         model_name='score',
    #         name='Score_9',
    #     ),
    #     migrations.AddField(
    #         model_name='comments',
    #         name='content',
    #         field=models.TextField(help_text="User's comment.", max_length=255, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='comments',
    #         name='dateOfCmt',
    #         field=models.DateField(blank=True, help_text="Comment's date.", null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='comments',
    #         name='likes',
    #         field=models.IntegerField(default=0, help_text='Number of likes.', null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='content',
    #         name='aired',
    #         field=models.CharField(blank=True, help_text='Publish date.', max_length=255, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='content',
    #         name='cType',
    #         field=models.CharField(blank=True, help_text='Manga type (Oneshot, shounen,...)', max_length=255, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='content',
    #         name='category',
    #         field=models.CharField(choices=[('anime', 'Anime'), ('manga', 'Manga')], default='anime', help_text='Content category', max_length=20, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='content',
    #         name='completed',
    #         field=models.IntegerField(default=0, help_text='Completed.', null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='content',
    #         name='dropped',
    #         field=models.IntegerField(default=0, help_text='Dropped.', null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='content',
    #         name='duration',
    #         field=models.CharField(blank=True, help_text='None for Manga.', max_length=255, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='content',
    #         name='episodes',
    #         field=models.IntegerField(blank=True, help_text='Number of published chapters.', null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='content',
    #         name='favorites',
    #         field=models.IntegerField(default=0, help_text='Number of user have this manga in their favorite list.', null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='content',
    #         name='genres',
    #         field=models.CharField(blank=True, help_text="Content's Genres", max_length=255, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='content',
    #         name='lastUpdate',
    #         field=models.DateField(blank=True, help_text='Date of last published chapter.', null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='content',
    #         name='licensors',
    #         field=models.CharField(blank=True, help_text='Companies that have the rights to translate, publish, and distribute the manga.', max_length=255, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='content',
    #         name='name',
    #         field=models.CharField(help_text='Content name', max_length=255, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='content',
    #         name='onHold',
    #         field=models.IntegerField(default=0, help_text='On Hold.', null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='content',
    #         name='picture',
    #         field=models.ImageField(blank=True, default=None, help_text='Content cover picture.', null=True, upload_to=''),
    #     ),
    #     migrations.AddField(
    #         model_name='content',
    #         name='planToWatch',
    #         field=models.IntegerField(default=0, help_text='Plan to Read.', null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='content',
    #         name='producers',
    #         field=models.CharField(blank=True, help_text='None for Manga.', max_length=500, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='content',
    #         name='ranked',
    #         field=models.IntegerField(default=0, help_text='.', null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='content',
    #         name='rating',
    #         field=models.CharField(blank=True, help_text='Manga age rate (e.g. safe).', max_length=255, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='content',
    #         name='scoreAvg',
    #         field=models.FloatField(default=0.0, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='content',
    #         name='source',
    #         field=models.CharField(blank=True, help_text='Light novel, Book, etc. (e.g Original).', max_length=255, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='content',
    #         name='studios',
    #         field=models.CharField(blank=True, help_text='Tteams that assist the main artist with tasks.', max_length=255, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='content',
    #         name='watching',
    #         field=models.IntegerField(default=0, help_text='Reading.', null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='feedback',
    #         name='cmt',
    #         field=models.TextField(blank=True, help_text='User comment about the product.', max_length=500, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='feedback',
    #         name='rate',
    #         field=models.IntegerField(blank=True, help_text='User rating of the product.', null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='notifications',
    #         name='date',
    #         field=models.DateField(help_text="Notification's arrived date.", null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='notifications',
    #         name='isRead',
    #         field=models.BooleanField(default=False, help_text="Notification's is readed by user or not.", null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='notifications',
    #         name='message',
    #         field=models.TextField(help_text="Notification's message.", max_length=500, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='notifications',
    #         name='nType',
    #         field=models.CharField(blank=True, help_text="Notification's type.", max_length=255, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='order',
    #         name='orderDate',
    #         field=models.DateField(help_text='Date of the order.', null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='order',
    #         name='status',
    #         field=models.CharField(help_text='Order status (e.g. Shipped).', max_length=255, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='orderitems',
    #         name='buyPrice',
    #         field=models.FloatField(help_text='Price at the time of Ordered.', null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='orderitems',
    #         name='quantity',
    #         field=models.IntegerField(default=1, help_text='Number of ordered products.', null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='product',
    #         name='description',
    #         field=models.TextField(blank=True, help_text="Product's description.", max_length=500, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='product',
    #         name='name',
    #         field=models.CharField(help_text='Name of the product.', max_length=255, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='product',
    #         name='picture',
    #         field=models.ImageField(blank=True, help_text="Product's picture.", null=True, upload_to=''),
    #     ),
    #     migrations.AddField(
    #         model_name='product',
    #         name='price',
    #         field=models.FloatField(default=0, help_text="Product's price.", null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='product',
    #         name='ravg',
    #         field=models.FloatField(default=0, help_text="Product's average rating.", null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='score',
    #         name='score1',
    #         field=models.IntegerField(default=0, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='score',
    #         name='score10',
    #         field=models.IntegerField(default=0, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='score',
    #         name='score2',
    #         field=models.IntegerField(default=0, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='score',
    #         name='score3',
    #         field=models.IntegerField(default=0, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='score',
    #         name='score4',
    #         field=models.IntegerField(default=0, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='score',
    #         name='score5',
    #         field=models.IntegerField(default=0, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='score',
    #         name='score6',
    #         field=models.IntegerField(default=0, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='score',
    #         name='score7',
    #         field=models.IntegerField(default=0, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='score',
    #         name='score8',
    #         field=models.IntegerField(default=0, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='score',
    #         name='score9',
    #         field=models.IntegerField(default=0, null=True),
    #     ),
    #     migrations.DeleteModel(
    #         name='favorite_list',
    #     ),
    #     migrations.DeleteModel(
    #         name='score_list',
    #     ),
    #     migrations.DeleteModel(
    #         name='user',
    #     ),
    #     migrations.AddField(
    #         model_name='scorelist',
    #         name='cid',
    #         field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scoreslist', to='wibu_catalog.content'),
    #     ),
    #     migrations.AddField(
    #         model_name='scorelist',
    #         name='uid',
    #         field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scoreslist', to='wibu_catalog.users'),
    #     ),
    #     migrations.AddField(
    #         model_name='favoritelist',
    #         name='cid',
    #         field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favlist', to='wibu_catalog.content'),
    #     ),
    #     migrations.AddField(
    #         model_name='favoritelist',
    #         name='uid',
    #         field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favlist', to='wibu_catalog.users'),
    #     ),
    #     migrations.AddField(
    #         model_name='comments',
    #         name='uid',
    #         field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='wibu_catalog.users'),
    #         preserve_default=False,
    #     ),
    #     migrations.AddField(
    #         model_name='feedback',
    #         name='uid',
    #         field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='wibu_catalog.users'),
    #         preserve_default=False,
    #     ),
    #     migrations.AddField(
    #         model_name='notifications',
    #         name='uid',
    #         field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='wibu_catalog.users'),
    #         preserve_default=False,
    #     ),
    #     migrations.AddField(
    #         model_name='order',
    #         name='uid',
    #         field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='wibu_catalog.users'),
    #         preserve_default=False,
    #     ),
    #     migrations.AlterUniqueTogether(
    #         name='scorelist',
    #         unique_together={('uid', 'cid')},
    #     ),
    ]
