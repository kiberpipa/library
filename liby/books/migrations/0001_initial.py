# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table('books_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('books', ['Author'])

        # Adding model 'Genre'
        db.create_table('books_genre', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gendre_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('books', ['Genre'])

        # Adding model 'Publisher'
        db.create_table('books_publisher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('books', ['Publisher'])

        # Adding model 'Item'
        db.create_table('books_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['books.Author'])),
            ('pub_date', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['books.Publisher'], null=True, blank=True)),
            ('gendre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['books.Genre'], null=True, blank=True)),
        ))
        db.send_create_signal('books', ['Item'])

        # Adding model 'Book'
        db.create_table('books_book', (
            ('item_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['books.Item'], unique=True, primary_key=True)),
            ('reading_room_only', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('available', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('reserved', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('books', ['Book'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table('books_author')

        # Deleting model 'Genre'
        db.delete_table('books_genre')

        # Deleting model 'Publisher'
        db.delete_table('books_publisher')

        # Deleting model 'Item'
        db.delete_table('books_item')

        # Deleting model 'Book'
        db.delete_table('books_book')


    models = {
        'books.author': {
            'Meta': {'object_name': 'Author'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'books.book': {
            'Meta': {'object_name': 'Book', '_ormbases': ['books.Item']},
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'item_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['books.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'reading_room_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reserved': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'books.genre': {
            'Meta': {'object_name': 'Genre'},
            'gendre_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'books.item': {
            'Meta': {'object_name': 'Item'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['books.Author']"}),
            'gendre': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['books.Genre']", 'null': 'True', 'blank': 'True'}),
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