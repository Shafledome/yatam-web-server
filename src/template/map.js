let myMap = L.map('map').setView([36.72, -4.42], 13)

L.tileLayer(`https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png`, {
	maxZoom: 18,
}).addTo(myMap);

let iconMarker = L.icon({
    iconUrl: 'marker.png',
    iconSize: [60, 60],
    iconAnchor: [30, 60]
})

let iconMuseum = L.icon({
    iconUrl: 'museum.jpg',
    iconSize: [60,60],
    iconAnchor: [30,60]
})

new Vue({
  el: '#app',
  data () {
    return {
      info: null
    }
  },
  mounted () {
    axios
      .get('https://api.coindesk.com/v1/bpi/currentprice.json')
      .then(response => (this.info = response))
  }
})

let marker2 = L.marker([36.72, -4.42], { icon: iconMarker }).addTo(myMap)


myMap.doubleClickZoom.disable()
/*myMap.on('dblclick', e => {
  let latLng = myMap.mouseEventToLatLng(e.originalEvent);

  L.marker([latLng.lat, latLng.lng], { icon: iconMarker }).addTo(myMap)
})*/

navigator.geolocation.getCurrentPosition(
  (pos) => {
    const { coords } = pos
    const { latitude, longitude } = coords
    L.marker([latitude, longitude], { icon: iconMuseum }).addTo(myMap)

    setTimeout(() => {
      myMap.panTo(new L.LatLng(latitude, longitude))
    }, 5000)
  },
  (error) => {
    console.log(error)
  },
  {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0
  })