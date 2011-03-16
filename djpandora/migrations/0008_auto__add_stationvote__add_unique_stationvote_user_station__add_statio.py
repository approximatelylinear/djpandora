# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'StationVote'
        db.create_table('djpandora_stationvote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['djpandora.Station'])),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('djpandora', ['StationVote'])

        # Adding unique constraint on 'StationVote', fields ['user', 'station']
        db.create_unique('djpandora_stationvote', ['user_id', 'station_id'])

        # Adding model 'StationPoll'
        db.create_table('djpandora_stationpoll', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['djpandora.Station'])),
            ('time_started', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('djpandora', ['StationPoll'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'StationVote', fields ['user', 'station']
        db.delete_unique('djpandora_stationvote', ['user_id', 'station_id'])

        # Deleting model 'StationVote'
        db.delete_table('djpandora_stationvote')

        # Deleting model 'StationPoll'
        db.delete_table('djpandora_stationpoll')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'djpandora.song': {
            'Meta': {'object_name': 'Song'},
            'album': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pandora_id': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['djpandora.Station']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'djpandora.station': {
            'Meta': {'object_name': 'Station'},
            'account': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'pandora_id': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'djpandora.stationpoll': {
            'Meta': {'object_name': 'StationPoll'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['djpandora.Station']"}),
            'time_started': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'djpandora.stationvote': {
            'Meta': {'unique_together': "(('user', 'station'),)", 'object_name': 'StationVote'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['djpandora.Station']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'djpandora.vote': {
            'Meta': {'unique_together': "(('user', 'song', 'station'),)", 'object_name': 'Vote'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['djpandora.Song']"}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['djpandora.Station']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['djpandora']
