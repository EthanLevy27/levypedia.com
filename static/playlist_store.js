function save(item){
    console.log("Writing stuff " + item.toString());
    $.post(
        '/songwrite/' + item, 
        {}, 
        (data, status, jqXhr) => {
            if(data == 200) {
                console.log("That worked!");
            } else {
                console.log("Error!");
            }
        }
    )
}

function loadPlaylist() {
    $.get('/songread',
        {},
        (data, status, jqXhr) => {
            if(data = 200) {
                console.log("That Worked");
            } else {
                console.log("Error!");
            }
        }
    )
}