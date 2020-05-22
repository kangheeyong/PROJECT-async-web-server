
console.log('123'+query)

var ws;
function init() {
    ws = new WebSocket("ws://localhost:8080/feed");
    ws.onmessage = function(event){ 
        console.log(event.data); 
        $('#table01').append(event.data+'<br />');
    }
}

$(document).ready(function(){
    $('#div01').scroll(function(){
        var scrollT = $(this).scrollTop(); 
        var scrollH = $(this).height(); 
        var contentH = $('#table01').height(); 
        if(scrollT + scrollH +1 >= contentH) { 
            var msg = {
                'scrollT': scrollT,
                'scrollH': scrollH,
                'contentH': contentH,
                'query': query
            };
            ws.send(JSON.stringify(msg))
        }
    });
});

if(query != ''){
    init();
}  
