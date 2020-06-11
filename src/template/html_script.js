var ws;
function init() {
    ws = new WebSocket("ws://localhost:8070/feed");
    ws.onmessage = function(event){ 
        $('#table01').append(event.data+'<br />');
    };
};
$(document).ready(function(){
    var contentH_before = 0
    $('#div01').scroll(function(){
        var scrollT = $(this).scrollTop(); 
        var scrollH = $(this).height(); 
        var contentH = $('#table01').height(); 
        if(scrollT + scrollH +1 >= contentH) { 
            var msg = {
                'scrollT': scrollT,
                'scrollH': scrollH,
                'contentH': contentH,
                'contentH_before': contentH_before,
                'query': query
            };
            if(contentH_before < contentH){
                ws.send(JSON.stringify(msg));
                contentH_before = contentH;
            };
        };
    });
});

if(query != ''){
    init();
}  
