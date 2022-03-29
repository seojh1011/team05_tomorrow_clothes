window.onresize = function (event) {
    translate_att();
}

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
    change_gps_kweather(latitude, longitude)
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
                console.log(data)

                for (let i = 0; i < data.length; i++) {
                    let img_url = data[i]["feeds_img_url"]
                    let id = data[i]["id"]
                    console.log(img_url);
                    let temp_img_div = `<div class="image" onclick="location.href='/detail/${id}/'"><img src="${img_url}"></div>`
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
    let imgStack = [0, 0, 0, 0, 0, 0];
    if (innerWidth >= 500) {
        imgStack = [0, 0, 0, 0, 0, 0];
        console.log('들어옴(큰창)')
    } else {
        imgStack = [0, 0];
        console.log('들어옴(작은창)')
    }

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
            console.log(data)
            console.log(data['address'])
            console.log(data['tmp'][0]['fcstValue'])
            $('.weather-icon').first().text(data['tmp'][0]['fcstValue']);
            let temp = temp_recomand(data['tmp'][0]['fcstValue'])
            $('.weather-icon:eq(2)').text(temp);
            $('.location:eq(0)').text(data['address']);
        }
    })
}

function temp_recomand(temp) {
    if (temp < 5) {
        return '겨울옷,방한용품'
    } else if (5 <= temp && temp < 10) {
        return '코트,가죽자켓'
    } else if (10 <= temp && temp < 12) {
        return '트렌치 코트, 야상 여러겹 껴입기'
    } else if (12 <= temp && temp < 17) {
        return '자켓, 셔츠, 가디건'
    } else if (17 <= temp && temp < 20) {
        return '니트,가디건, 후드티, 맨투맨, 청바지, 면바지'
    } else if (20 <= temp && temp < 23) {
        return '긴팔, 가디건, 후드티, 면바지, 슬랙스, 스키니'
    } else if (23 <= temp && temp < 26) {
        return '반팔, 얇은 셔츠, 긴팔, 반바지, 면바지'
    } else if (26 <= temp && temp < 27) {
        return '민소매, 반바지, 원피스'
    }
}


function translate_att() {
    let images = document.querySelectorAll(".image");
    let imgStack = [0, 0, 0, 0, 0, 0];
    let innerWidth = window.innerWidth;

    console.log('innerWidth' + innerWidth)
    console.log('type innerWidth' + typeof innerWidth)

    if (innerWidth >= 500) {
        imgStack = [0, 0, 0, 0, 0, 0];
        console.log('들어옴(큰창)')
    } else {
        imgStack = [0, 0];
        console.log('들어옴(작은창)')
    }

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