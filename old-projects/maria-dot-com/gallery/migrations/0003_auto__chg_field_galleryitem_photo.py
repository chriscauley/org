# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'GalleryItem.photo'
        db.alter_column('gallery_galleryitem', 'photo_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['photo.Photo']))
    def backwards(self, orm):

        # Changing field 'GalleryItem.photo'
        db.alter_column('gallery_galleryitem', 'photo_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photo.Photo'], null=True))
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
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photo.Photo']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.GallerySection']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '128', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
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
            'landscape_crop': ('crop_override.field.CropOverride', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'portrait_crop': ('crop_override.field.CropOverride', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'square_crop': ('crop_override.field.CropOverride', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'src': ('crop_override.field.OriginalImage', [], {'max_length': '300'})
        }
    }

    complete_apps = ['gallery']