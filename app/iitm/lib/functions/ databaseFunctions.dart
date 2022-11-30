import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/foundation.dart';

create_alert(double lat, double long, uid,String location) async {
  await FirebaseFirestore.instance
      .collection('alerts')
      .add({'lat': lat, 'long': long, 'time': FieldValue.serverTimestamp(),'uid':uid,'location':location});
  print('Database Updated');
}