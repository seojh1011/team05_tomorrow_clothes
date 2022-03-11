//좋아요 구현
function scraps(on_off) {
    console.log("test color : ", on_off.style.color);

    let likes = document.getElementById("icon_scraps").innerText
    let scrap = document.getElementById("scrap")

    if (on_off.style.color === "yellow") {
        scrap.className = "far fa-star";

        on_off.style.color = "lightgray";
        document.getElementById("icon_scraps").innerText = parseInt(likes) - 1;
        /*
        $.ajax({
            url: api,
            type: 'post',
            data: {"like": "on"},
            success: function (data) {
                console.log(data);
            }
        });
        */

    } else if (on_off.style.color === "" || on_off.style.color === "lightgray") {
        scrap.className = "fas fa-star";
        on_off.style.color = "yellow";
        document.getElementById("icon_scraps").innerText = parseInt(likes) + 1;
        /*$.ajax({
            url: api,
            type: 'post',
            data: {"like": "off"},
            success: function (data) {
                console.log(data);
            }
        });*/
    }
}