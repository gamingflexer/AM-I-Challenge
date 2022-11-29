const uluru = { lat: -25.344, lng: 131.031 };
console.log(typeof parseFloat(lat_user));
console.log(lng_user)

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

    function addmarker(location, link) {
        var marker = new google.maps.Marker({
            position: location,
            map: map,
            icon: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png'
        });

        const detailsWindows = new google.maps.InfoWindow({
            content: `<h1 style="color:rgb(255, 255, 255)"><a href="${link}">Heading</a></h1>`
        });

        marker.addListener("click", () => {
            detailsWindows.open(map, marker);
        })
    }

    addmarker(uluru, "http://www.google.com/");
    addmarker({lat: parseFloat(lat_user), lng: parseFloat(lng_user)}, "http://www.asach.co/");
}


window.initMap = initMap;