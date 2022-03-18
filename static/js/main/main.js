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
            $('.weather-icon:eq(1)').empty();
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