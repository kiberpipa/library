# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Genre.gendre_name'
        db.delete_column('books_genre', 'gendre_name')

        # Adding field 'Genre.genre_name'
        db.add_column('books_genre', 'genre_name',
                      self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=20),
                      keep_default=False)

        # Deleting field 'Item.gendre'
        db.delete_column('books_item', 'gendre_id')

        # Adding M2M table for field genres on 'Item'
        db.create_table('books_item_genres', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(orm['books.item'], null=False)),
            ('genre', models.ForeignKey(orm['books.genre'], null=False))
        ))
        db.create_unique('books_item_genres', ['item_id', 'genre_id'])


    def backwards(self, orm):
        # Adding field 'Genre.gendre_name'
        db.add_column('books_genre', 'gendre_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20),
                      keep_default=False)

        # Deleting field 'Genre.genre_name'
        db.delete_column('books_genre', 'genre_name')

        # Adding field 'Item.gendre'
        db.add_column('books_item', 'gendre',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['books.Genre'], null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field genres on 'Item'
        db.delete_table('books_item_genres')


    models = {
        'books.author': {
            'Meta': {'object_name': 'Author'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'books.book': {
            'Meta': {'object_name': 'Book', '_ormbases': ['books.Item']},
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'item_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['books.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'reading_room_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reserved': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'books.genre': {
            'Meta': {'object_name': 'Genre'},
            'genre_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'books.item': {
            'Meta': {'object_name': 'Item'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'item_authors_set'", 'symmetrical': 'False', 'to': "orm['books.Author']"}),
            'genres': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'item_genres_set'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['books.Genre']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['books.Publisher']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'books.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['books']