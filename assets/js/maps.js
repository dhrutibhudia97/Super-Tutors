function initMap() {
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 14, 
        center: {
            lat: 51.550513,
            lng: -0.304841
        }
    });

    var labels = "ABC";

    var locations = [
        { lat: 51.550523, lng: -0.304891}
    ];

    var markers = locations.map(function(location, i) {
        return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length]
        });
    });

    var markerCluster = new MarkerClusterer(map, markers,
    {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});
}

        
