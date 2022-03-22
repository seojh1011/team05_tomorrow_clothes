window.onload = () => {
    translate_att();

    /*테스트 온도 API 스파르타 꺼.*/

    $.ajax({
        type: "GET",
        url: "http://spartacodingclub.shop/sparta_api/weather/seoul",
        data: {},
        success: function (response) {
            console.log(response)
            $('.location:eq(0)').text(response['city']);
            $('.weather-icon').first().text(response['temp']);
            //해당 객체 지우고 실행
            $('.weather-icon:eq(1)').empty();
            //객체 위에 다시 작성
            $('.weather-icon:eq(1)').append(`<img src="${response['icon']}" style ="width: 40px;"></img>`);
            $('.weather-icon:eq(2)').text(response['clouds']);
        }
    })


    function translate_att() {
        let images = document.querySelectorAll(".image");
        let imgStack = [0, 0];
        let colWidth = 170;
        for (let i = 0; i < images.length; i++) {
            let minIndex = imgStack.indexOf(Math.min.apply(0, imgStack));
            let x = colWidth * minIndex;
            let y = imgStack[minIndex];
            imgStack[minIndex] += (images[i].children[0].height + 10);
            images[i].style.transform = `translateX(${x}px) translateY(${y}px)`;
            if (i === images.length - 1) {
                document.querySelector(".images").style.height = `${Math.max.apply(0, imgStack)}px`;
            }
        }
    }
}


let state = false;
let timer_state = true;
var page_num = 2;
let latitude = 0;
let longitude = 0;
//현재 위치 가져오는 기능
navigator.geolocation.getCurrentPosition(function (pos) {
    latitude = pos.coords.latitude;
    longitude = pos.coords.longitude;
    console.log("현재 위치는 : " + latitude + ", " + longitude);
});

//웹 페이지가 준비가 되면 실행하는 이벤트
window.addEventListener('load', function () {

    let feed = document.getElementsByTagName('div')[0];
    //feed 스크롤이 움직이면 실행하는 이벤트
    feed.addEventListener('scroll', function () {
            console.log('timer_state : ' + timer_state)
            if (timer_state === true) {
                timer_state = false;
                setTimeout(function () {
                    scroller_delay();
                    setTimeout(function () {
                        translate_att2();
                    }, 500)
                    timer_state = true;
                }, 500);

            }
        }
    )

    //스크롤 위치를 감지해서 delay를 주고 페이지를 가져오는 함수
    function scroller_delay() {
        console.log('timer_state2 : ' + timer_state)
        let currentScrollValue = document.getElementById('body_container').scrollTop;
        let ScrollHighValue = document.getElementById('body_container').scrollHeight;
        let actingScroll = ScrollHighValue - currentScrollValue;
        const clientHeight = document.getElementsByTagName('body')[0].clientHeight;
        // console.log('스크롤 위치는 :' + currentScrollValue);
        // console.log('스크롤 크기는 :' + ScrollHighValue);
        // console.log('전체 크기 : ' + clientHeight);
        // console.log('스크롤 위치 - 스크롤크기 == 전체크기 : ' + actingScroll);
        if (clientHeight + 10 >= actingScroll) {
            state = true;
            // console.log('state start ~!!!!!! :' + state);
            get_page(latitude, longitude)
        }
    }

    //FEED불러 오는 함수
    function get_page(x, y) {

        $.ajax({
            url: "/",
            data: {'page': page_num, 'limit': 20, 'x': x, 'y': y},
            method: 'GET',
            dataType: "json",
            success: function (data) {

                for (let i = 0; i < data.length; i++) {
                    let img_url = data[i]["feeds_img_url"]
                    console.log(img_url);
                    let temp_img_div = `<div class="image"><img src="${img_url}"></div>`
                    $('#images_box').append(temp_img_div);
                }
                page_num++;
            }
        })
    }
});

// 불러온 FEED위에 스타일 적용하는 태그
function translate_att2() {
    console.log("실행 되고 있음22222222222222");
    let images = document.querySelectorAll(".image");
    console.log("실행 되고 있음");
    let imgStack = [0, 0];
    console.log("실행");
    let colWidth = 170;
    for (let i = 0; i < images.length; i++) {
        let minIndex = imgStack.indexOf(Math.min.apply(0, imgStack));
        let x = colWidth * minIndex;
        let y = imgStack[minIndex];
        imgStack[minIndex] += (images[i].children[0].height + 10);
        images[i].style.transform = `translateX(${x}px) translateY(${y}px)`;
        if (i === images.length - 1) {
            document.querySelector(".images").style.height = `${Math.max.apply(0, imgStack)}px`;
        }
    }
}


function change_gps_kweather(latitude, longitude) {
    $.ajax({
            url: "k-weather/",
            data: {'x': longitude, 'y': latitude},
            method: 'post',
            dataType: "json",
            success: function (data) {


            }
        })
}

