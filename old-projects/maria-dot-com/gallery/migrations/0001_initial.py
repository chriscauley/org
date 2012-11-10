# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Gallery'
        db.create_table('gallery_gallery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=99999)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=128, unique=True, null=True, blank=True)),
            ('src', self.gf('sorl.thumbnail.fields.ImageField')(max_length=300)),
        ))
        db.send_create_signal('gallery', ['Gallery'])

        # Adding model 'GallerySection'
        db.create_table('gallery_gallerysection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=99999)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=128, unique=True, null=True, blank=True)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Gallery'])),
            ('src', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photo.Photo'])),
            ('hover', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['photo.Photo'])),
            ('left', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('top', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('gallery', ['GallerySection'])

        # Adding model 'GalleryItem'
        db.create_table('gallery_galleryitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=99999)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=128, unique=True, null=True, blank=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.GallerySection'])),
            ('src', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photo.Photo'], null=True, blank=True)),
        ))
        db.send_create_signal('gallery', ['GalleryItem'])

    def backwards(self, orm):
        # Deleting model 'Gallery'
        db.delete_table('gallery_gallery')

        # Deleting model 'GallerySection'
        db.delete_table('gallery_gallerysection')

        # Deleting model 'GalleryItem'
        db.delete_table('gallery_galleryitem')

    models = {
        'gallery.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '99999'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '128', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'src': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '300'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'gallery.galleryitem': {
            'Meta': {'object_name': 'GalleryItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '99999'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.GallerySection']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '128', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'src': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photo.Photo']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'gallery.gallerysection': {
            'Meta': {'ordering': "('order',)", 'object_name': 'GallerySection'},
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Gallery']"}),
            'hover': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['photo.Photo']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'left': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '99999'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '128', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'src': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photo.Photo']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'top': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'photo.photo': {
            'Meta': {'object_name': 'Photo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'src': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['gallery']