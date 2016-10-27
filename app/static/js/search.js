var btSearch = document.getElementById("btSearch");
var header = new Headers({
    "Content-Type": "application/json",
});
var init = {
    method: 'GET',
    headers: header,
    mods: 'no-cors',
    cache: 'default'
}

btSearch.addEventListener('click', search);
function search() {
    // 接受表单提供的数据
    var name = document.getElementById("name").value;
    fetch('http://p.muxixyz.com/api/sid/?name='+name, init)
    .then(function (res) {
        return res.json();
    })
    .then(function (json) {
        sids = json.sids;
        $("#xoimg").empty();
        for(var i=0, l=sids.length; i<l; i++) {
            // var img = document.createElement('img');
            var sid = sids[i]['sid'];           // 学号
            var deptName = sids[i]['deptName']; // 专业
            var orgName = sids[i]['orgName'];   // 爱吃
            var src = "http://xssw.ccnu.edu.cn:8001/xgxt/xsxx_xsgl.do?method=showPhoto&xh=" + sid;
            var _code = '<div class="media"><div class="media-left"><img src='+src+' height="200px" width="200px"></div><div class="media-body"><div class="media-heading">'+name+' @'+sid+'</div><div class="media-content"><hr/><li>-专业: '+deptName+'<br/>-爱吃: '+ orgName +'</li></div></div></div>';
            $("#xoimg").append(_code);
            alert("准备亮瞎你的🐶 眼!");
        }
    });
}
