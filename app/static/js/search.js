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
    fetch('http://7xj431.com1.z0.glb.clouddn.com/tt.gif', init)
    .then(function (res) {
        return res.blob();
    })
    .then(function (blob) {
        var objectURL = URL.createObjectURL(blob);
        image.src = objectURL;
    });
}
