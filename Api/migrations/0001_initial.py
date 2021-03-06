# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'tempUser'
        db.create_table(u'Api_tempuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=100)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('DateTimeCreated', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'Api', ['tempUser'])

        # Adding model 'Profile'
        db.create_table(u'Api_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=100)),
            ('confirmationCode', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('authToken', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'Api', ['Profile'])

        # Adding model 'Team'
        db.create_table(u'Api_team', (
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200, primary_key=True)),
        ))
        db.send_create_signal(u'Api', ['Team'])

        # Adding model 'LeagueType'
        db.create_table(u'Api_leaguetype', (
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200, primary_key=True)),
        ))
        db.send_create_signal(u'Api', ['LeagueType'])

        # Adding model 'League'
        db.create_table(u'Api_league', (
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200, primary_key=True)),
            ('countryFlagUrl', self.gf('django.db.models.fields.files.ImageField')(default='flags/none/no-img.jpg', max_length=100)),
        ))
        db.send_create_signal(u'Api', ['League'])

        # Adding model 'PredictionDetail'
        db.create_table(u'Api_predictiondetail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('message', self.gf('django.db.models.fields.TextField')(max_length=1000)),
        ))
        db.send_create_signal(u'Api', ['PredictionDetail'])

        # Adding model 'Unit'
        db.create_table(u'Api_unit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'Api', ['Unit'])

        # Adding model 'CompletedText'
        db.create_table(u'Api_completedtext', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'Api', ['CompletedText'])

        # Adding model 'Prediction'
        db.create_table(u'Api_prediction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('leagueType', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Api.LeagueType'])),
            ('league', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Api.League'])),
            ('flagURL', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('homeTeam', self.gf('django.db.models.fields.related.ForeignKey')(related_name='statusPrediction_home_team', to=orm['Api.Team'])),
            ('awayTeam', self.gf('django.db.models.fields.related.ForeignKey')(related_name='statusPrediction_away_team', to=orm['Api.Team'])),
            ('tipDetail', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Api.PredictionDetail'])),
            ('isPushNotifSend', self.gf('django.db.models.fields.BooleanField')()),
            ('isCompleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('completedText', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Api.CompletedText'])),
            ('DateTimeCreated', self.gf('django.db.models.fields.DateTimeField')()),
            ('DateTimeCompleted', self.gf('django.db.models.fields.DateTimeField')()),
            ('isPredictionVerified', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('verified', self.gf('django.db.models.fields.BooleanField')()),
            ('covered', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'Api', ['Prediction'])

        # Adding model 'PurchasedPrediction'
        db.create_table(u'Api_purchasedprediction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('userID', self.gf('django.db.models.fields.IntegerField')()),
            ('predictionID', self.gf('django.db.models.fields.IntegerField')()),
            ('DateTime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'Api', ['PurchasedPrediction'])


    def backwards(self, orm):
        # Deleting model 'tempUser'
        db.delete_table(u'Api_tempuser')

        # Deleting model 'Profile'
        db.delete_table(u'Api_profile')

        # Deleting model 'Team'
        db.delete_table(u'Api_team')

        # Deleting model 'LeagueType'
        db.delete_table(u'Api_leaguetype')

        # Deleting model 'League'
        db.delete_table(u'Api_league')

        # Deleting model 'PredictionDetail'
        db.delete_table(u'Api_predictiondetail')

        # Deleting model 'Unit'
        db.delete_table(u'Api_unit')

        # Deleting model 'CompletedText'
        db.delete_table(u'Api_completedtext')

        # Deleting model 'Prediction'
        db.delete_table(u'Api_prediction')

        # Deleting model 'PurchasedPrediction'
        db.delete_table(u'Api_purchasedprediction')


    models = {
        u'Api.completedtext': {
            'Meta': {'object_name': 'CompletedText'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'Api.league': {
            'Meta': {'object_name': 'League'},
            'countryFlagUrl': ('django.db.models.fields.files.ImageField', [], {'default': "'flags/none/no-img.jpg'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'primary_key': 'True'})
        },
        u'Api.leaguetype': {
            'Meta': {'object_name': 'LeagueType'},
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'primary_key': 'True'})
        },
        u'Api.prediction': {
            'DateTimeCompleted': ('django.db.models.fields.DateTimeField', [], {}),
            'DateTimeCreated': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'Prediction'},
            'awayTeam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statusPrediction_away_team'", 'to': u"orm['Api.Team']"}),
            'completedText': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Api.CompletedText']"}),
            'covered': ('django.db.models.fields.BooleanField', [], {}),
            'flagURL': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'homeTeam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statusPrediction_home_team'", 'to': u"orm['Api.Team']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isCompleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isPredictionVerified': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'isPushNotifSend': ('django.db.models.fields.BooleanField', [], {}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Api.League']"}),
            'leagueType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Api.LeagueType']"}),
            'tipDetail': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Api.PredictionDetail']"}),
            'verified': ('django.db.models.fields.BooleanField', [], {})
        },
        u'Api.predictiondetail': {
            'Meta': {'object_name': 'PredictionDetail'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'Api.profile': {
            'Meta': {'object_name': 'Profile'},
            'authToken': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'confirmationCode': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'Api.purchasedprediction': {
            'DateTime': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'PurchasedPrediction'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'predictionID': ('django.db.models.fields.IntegerField', [], {}),
            'userID': ('django.db.models.fields.IntegerField', [], {})
        },
        u'Api.team': {
            'Meta': {'object_name': 'Team'},
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'primary_key': 'True'})
        },
        u'Api.tempuser': {
            'DateTimeCreated': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'tempUser'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'Api.unit': {
            'Meta': {'object_name': 'Unit'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['Api']