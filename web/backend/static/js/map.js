const uluru = { lat: -25.344, lng: 131.031 };
console.log(typeof parseFloat(lat_user));
console.log(lng_user)
console.log(des)

function initMap() {

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 2,
        center: new google.maps.LatLng(35.55, -25.75),
        mapTypeId: google.maps.MapTypeId.ROADMAP
    });


    // const detailsWindows = new google.maps.InfoWindow({
    //     content : `<h3><a href="http://www.google.com/">heading</a></h3>`
    //   });

    //   marker.addListener("click", () =>{
    //     detailsWindows.open(map, marker);
    //   })
//https://firebasestorage.googleapis.com/v0/b/hackmanthan-lostminds.appspot.com/o/map-pin.svg?alt=media&token=80250171-c867-4537-8a0a-7704243c40d8
    function addmarker_user(location, link) {
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

    addmarker_user({lat: parseFloat(lat_user), lng: parseFloat(lng_user)}, "http://www.google.com/",des);

    function addmarker_cameras(location, link) {
        var marker = new google.maps.Marker({
            position: location,
            map: map,
            icon: 'https://firebasestorage.googleapis.com/v0/b/hackmanthan-lostminds.appspot.com/o/map-pin.svg?alt=media&token=80250171-c867-4537-8a0a-7704243c40d8'
        });

        const detailsWindows = new google.maps.InfoWindow({
            content: `<h1 style="color:rgb(255, 255, 255)"><a href="${link}">Heading</a></h1>`
        });

        marker.addListener("click", () => {
            detailsWindows.open(map, marker);
        })
    }
}


window.initMap = initMap;