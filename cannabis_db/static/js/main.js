
let map;

async function initiateTheMap() {
const { Map } = await google.maps.importLibrary("maps");

map = new Map(document.getElementById("map"), {
    center: { lat: 40.74527784245027, lng: -73.99032458586362 },
    mapId:'',
    zoom: 14,
    styles: [
                {
                    "featureType": "all",
                    "elementType": "labels.text.fill",
                    "stylers": [
                        {
                            "color": "#000"
                        }
                    ]
                },
                {},
        ]
  });
}