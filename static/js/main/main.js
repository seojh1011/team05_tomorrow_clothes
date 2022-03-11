 window.onload = () => {
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