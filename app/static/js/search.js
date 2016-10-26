var btSearch = document.getElementById("btSearch");
var imageF = document.getElementsByClassName("media-left");
var image = document.querySelector('img');
// var header = new Headers();
var init = {
    method: 'GET',
//    headers: header,
    mods: 'no-cors',
    cache: 'default'
}

btSearch.addEventListener('click', search);
function search() {
    fetch('http://127.0.0.1:5000/sid/', init)
    .then(function (res) {
        return res.json();
    })
    .then(function (json) {
        sids = json.get('sids');
        alert(sids.join());
    });
}
