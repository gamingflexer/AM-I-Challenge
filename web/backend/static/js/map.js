const uluru = { lat: -25.344, lng: 131.031 };
// var a = Array.from(JSON.parse(cords_var))

var camera = JSON.parse(cords_var.replace(/&quot;/ig,'"'));
// console.log(camera);

function initMap() {

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: new google.maps.LatLng(12.9941,80.1709),
        mapTypeId: google.maps.MapTypeId.ROADMAP
    });

    
    function addmarker_user(location, link) {
        var marker = new google.maps.Marker({
            position: location,
            map: map,
            icon: 'https://firebasestorage.googleapis.com/v0/b/hackmanthan-lostminds.appspot.com/o/map-pin.svg?alt=media&token=80250171-c867-4537-8a0a-7704243c40d8'
        });

        const detailsWindows = new google.maps.InfoWindow({
            content: `<h1 style="color:rgb(255, 255, 255)"><a href="${link}">${des}</a></h1>`
        });

        marker.addListener("click", () => {
            detailsWindows.open(map, marker);
        })
    }

    addmarker_user({lat: parseFloat(lat_user), lng: parseFloat(lng_user)},"","des");

    function addmarker_cameras(location, link,des) {
        var marker = new google.maps.Marker({
            position: location,
            map: map,
            icon: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png'
        });

        const detailsWindows = new google.maps.InfoWindow({
            content: `<h1 style="color:rgb(255, 255, 255)"><a href="${link}">${des}</a></h1>`
        });

        marker.addListener("click", () => {
            detailsWindows.open(map, marker);
        })
    }
    console.log(camera);
    addmarker_cameras({ lat: parseFloat(camera[0].lat), lng: parseFloat(camera[0].long) }, camera[0].camera_ip,`${camera[0].location} - ${camera[0].description}`);
    addmarker_cameras({ lat: parseFloat(camera[1].lat), lng: parseFloat(camera[1].long) }, camera[1].camera_ip,`${camera[1].location} - ${camera[1].description}`);
    addmarker_cameras({ lat: parseFloat(camera[2].lat), lng: parseFloat(camera[2].long) }, camera[2].camera_ip,`${camera[2].location} - ${camera[2].description}`);
    addmarker_cameras({ lat: parseFloat(camera[3].lat), lng: parseFloat(camera[3].long) }, camera[3].camera_ip,`${camera[3].location} - ${camera[3].description}`);
    addmarker_cameras({ lat: parseFloat(camera[4].lat), lng: parseFloat(camera[4].long) }, camera[4].camera_ip,`${camera[4].location} - ${camera[4].description}`);
    addmarker_cameras({ lat: parseFloat(camera[5].lat), lng: parseFloat(camera[5].long) }, camera[5].camera_ip,`${camera[5].location} - ${camera[5].description}`);
    addmarker_cameras({ lat: parseFloat(camera[6].lat), lng: parseFloat(camera[6].long) }, camera[6].camera_ip,`${camera[6].location} - ${camera[6].description}`);
}


window.initMap = initMap;