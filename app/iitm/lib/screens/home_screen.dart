import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:google_signin/screens/google_login.dart';
import 'package:google_signin/services/firebase_services.dart';
import 'package:geolocator/geolocator.dart';
import 'package:geocoding/geocoding.dart';
import '../functions/ databaseFunctions.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  User? user = FirebaseAuth.instance.currentUser;

// Check if the user is signed in
  void get_user_details_create_alert() {
    if (user != null) {
      String uid = user!.uid; // <-- User ID
      String? email = user!.email; // <-- Their email
    }
    getCurrentLocation();
    create_alert(_currentPosition.latitude, _currentPosition.longitude, user!.uid);
  }

  final geolocator =
      Geolocator.getCurrentPosition(forceAndroidLocationManager: true);
  late Position _currentPosition;
  String currentAddress = "";

  void getCurrentLocation() async {
    LocationPermission asked = await Geolocator.requestPermission();
    Geolocator.getCurrentPosition(desiredAccuracy: LocationAccuracy.high)
        .then((Position position) {
      setState(() {
        _currentPosition = position;
      });

      getAddressFromLatLng();
    }).catchError((e) {
      print(e);
    });
  }

  void getAddressFromLatLng() async {
    try {
      List<Placemark> p = await placemarkFromCoordinates(
          _currentPosition.latitude, _currentPosition.longitude);

      Placemark place = p[0];

      setState(() {
        currentAddress =
            "${place.thoroughfare} ${place.subThoroughfare} ${place.name} ${place.subLocality}";
      });
    } catch (e) {
      print(e);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Image.network(FirebaseAuth.instance.currentUser!.photoURL!),
            SizedBox(
              height: 20,
            ),
            Text("${FirebaseAuth.instance.currentUser!.displayName}"),
            Text("${FirebaseAuth.instance.currentUser!.email}"),
            SizedBox(
              height: 20,
            ),
            ElevatedButton(
              child: Text("Logout"),
              onPressed: () async {
                await FirebaseServices().googleSignOut();
                Navigator.push(
                    context,
                    MaterialPageRoute(
                        builder: (context) => GoogleLoginScreen()));
              },
            ),
            ElevatedButton(
              child: Text("Send Location"),
              onPressed: get_user_details_create_alert,
            ),
            // if (_currentPosition != null && currentAddress != null)
            Text(currentAddress,
                style: TextStyle(
                  fontSize: 20.0,
                  fontWeight: FontWeight.bold,
                )),
            // else
            //   Text("Could'nt fetch the location"),
          ],
        ),
      ),
    );
  }
}
