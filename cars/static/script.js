let menu = document.querySelector('#menu-btn');
let navbar = document.querySelector('.navbar');
let search = document.querySelector('.search-box');
let searchInput = document.querySelector('#search-input');

menu.onclick = () => {
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
};

document.querySelector('#login-btn').onclick = () => {
    document.querySelector(".login-form-container").classList.toggle('active');
};

document.querySelector('#close-login-form').onclick = () => {
    document.querySelector(".login-form-container").classList.remove('active');
};

window.onscroll = () => {
    if (window.scrollY > 0) {
        document.querySelector('.header').classList.add('active');
    } else {
        document.querySelector('.header').classList.remove('active');
    }
};

window.onload = () => {
    if (window.scrollY > 0) {
        document.querySelector('.header').classList.add('active');
    } else {
        document.querySelector('.header').classList.remove('active');
    }
};

document.querySelector('#search-btn').onclick = () => {
    search.classList.toggle('active');
    searchInput.focus(); // Automatically focus on the search input when the search button is clicked
};

searchInput.addEventListener('input', performSearch);

function performSearch() {
    const searchQuery = searchInput.value.toLowerCase();
    const allElements = document.querySelectorAll('body *');

    allElements.forEach((element) => {
        const elementText = element.innerText.toLowerCase();

        if (elementText.includes(searchQuery)) {
            element.style.display = 'block';
        } else {
            element.style.display = 'none';
        }
    });
}

var swiper = new Swiper(".vehicles-slider", {
    slidesPerView: 1,
    spaceBetween: 10,
    loop: true,
    grabCursor: true,
    centeredSlides: true,
    autoplay: {
        delay: 9500,
        disableOnInteraction: false,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    breakpoints: {
        0: {
            slidesPerView: 1,
        },
        768: {
            slidesPerView: 2,
        },
        991: {
            slidesPerView: 3,
        },
    },
});

var swiper = new Swiper(".review-slider", {
    grabCursor: true,
    centeredSlides: true,
    spaceBetween: 20,
    loop: true,
    autoplay: {
        delay: 9500,
        disableOnInteraction: false,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    breakpoints: {
        0: {
            slidesPerView: 1,
        },
        768: {
            slidesPerView: 2,
        },
        1024: {
            slidesPerView: 3,
        },
    },
});





// let searchBtn = document.querySelector('#search-btn');
// let searchInput = document.querySelector('#search-input');

// searchBtn.addEventListener('click', performSearch);
// searchInput.addEventListener('keyup', performSearch);

// function performSearch() {
//     let searchQuery = searchInput.value.trim().toLowerCase();
//     let elementsToSearch = Array.from(document.querySelectorAll('body *'));

//     elementsToSearch.forEach((element) => {
//         let elementText = element.innerText.toLowerCase();

//         if (elementText.includes(searchQuery)) {
//             highlightText(element, searchQuery);
//         } else {
//             removeHighlight(element);
//         }
//     });
// }

// function highlightText(element, searchQuery) {
//     let regex = new RegExp(searchQuery, 'gi');
//     let highlightedText = element.innerText.replace(regex, (match) => `<span class="highlight">${match}</span>`);
//     element.innerHTML = highlightedText;
// }

// function removeHighlight(element) {
//     element.innerHTML = element.innerText;
// }












var car =[{
    "id": 0,
    "name":"",
    "Varient_Name":"",
    "Model_Name":"",
    "Body_Type":"",
    "Price":"",
    "Waiting_Period":"",
    "Transmission":"",
    "Fuel Type":"",
    "Length":"",
    "Width":"",
    "Height":"",
    "Engine_CC":"",
    "Mileage":"",
    "Boot_Space":"",
    "Seats":"",
    "Airbags":"",
    "Camera":"",
    "HeadLight":"",
    "Rating":"",
    "image":"C:\\Users\\Dell\\Downloads\\image_placeholder.jpeg"
},{
    "id": 1,
    "name":"Hyundai Creta",
    "Varient_Name":"SX O 1.4 Turbo 7 DCT",
    "Model_Name":"Creta",
    "Body_Type":"suv",
    "Price":"10.44 Lakh",
    "Waiting_Period":"24 Weeks",
    "Transmission":"Automatic",
    "Fuel_Type":"Petrol",
    "Length":"4300 cm",
    "Width":"1790 cm",
    "Height":"1635 cm",
    "Engine_CC":"1353",
    "Mileage":"17 km/pl",
    "Boot_Space":"433 L",
    "Seats":"5",
    "Airbags":"6",
    "Camera":"Reverse",
    "HeadLight":"LED",
    "Rating":"4.5",
    "image":"{% static 'images/car_1.jpg' %}"
},{
    "id": 2,
    "name":"Hyundai Creta",
    "Varient_Name":"E 1.5 Diesel",
    "Model_Name":"Creta",
    "Body_Type":"suv",
    "Price":"10.44 Lakh",
    "Waiting_Period":"24 Weeks",
    "Transmission":"Manual",
    "Fuel_Type":"Diesel",
    "Length":"4300 cm",
    "Width":"1790 cm",
    "Height":"1635 cm",
    "Engine_CC":"1493",
    "Mileage":"21 km/pl",
    "Boot_Space":"433 L",
    "Seats":"5",
    "Airbags":"2",
    "Camera":"No",
    "HeadLight":"Halogen Projector",
    "Rating":"4.5",
    "image":"C:\\Users\\Dell\\Downloads\\creta.jpg"
},{
    "id": 3,
    "name":"Maruti Suzuki Grand Vitara",
    "Varient_Name":"Sigma Samrt Hybrid",
    "Model_Name":"Grand Vitara",
    "Body_Type":"SUV",
    "Price":"10.45 Lakh",
    "Waiting_Period":"23 Weeks",
    "Transmission":"Manual",
    "Fuel_Type":"Petrol",
    "Length":"4345 cm",
    "Width":"1795 cm",
    "Height":"1645 cm",
    "Engine_CC":"1462",
    "Mileage":"21.11 km/pl",
    "Boot_Space":"373 L",
    "Seats":"5",
    "Airbags":"2",
    "Camera":"No",
    "HeadLight":"Halogen",
    "Rating":"4.1",
    "image":"C:\\Users\\Dell\\Downloads\\grandvitara.png"
},{
    "id": 4,
    "name":"Maruti Suzuki Grand Vitara",
    "Varient_Name":"Alpha Plus Intelligent Hybrid ECVT",
    "Model_Name":"Grand Vitara",
    "Body_Type":"SUV",
    "Price":"10.45 Lakh",
    "Waiting_Period":"23 Weeks",
    "Transmission":"Automatic",
    "Fuel_Type":"Petrol",
    "Length":"4345 cm",
    "Width":"1795 cm",
    "Height":"1645 cm",
    "Engine_CC":"1490",
    "Mileage":"27.97 km/pl",
    "Boot_Space":"265 L",
    "Seats":"5",
    "Airbags":"6",
    "Camera":"360 Degree",
    "HeadLight":"LED",
    "Rating":"4.1",
    "image":"C:\\Users\\Dell\\Downloads\\grandvitara.png"
},{
    "id": 5,
    "name":"Maruti Suzuki Swift",
    "Varient_Name":"ZXI Plus AMT",
    "Model_Name":"Swift",
    "Body_Type":"Hatch back",
    "Price":"7.11 Lakh",
    "Waiting_Period":"9 Weeks",
    "Transmission":"Automatic",
    "Fuel_Type":"Petrol",
    "Length":"3845 cm",
    "Width":"1735 cm",
    "Height":"1530 cm",
    "Engine_CC":"1197 ",
    "Mileage":"22.56 km/pl",
    "Boot_Space":"268 L",
    "Seats":"5",
    "Airbags":"2",
    "Camera":"Reverse",
    "HeadLight":"LED Projector",
    "Rating":"4.4",
    "image":"C:\\Users\\Dell\\Downloads\\swift.jpg"
},{
    "id": 6,
    "name":"Maruti Suzuki Swift",
    "Varient_Name":"UXI",
    "Model_Name":"Swift",
    "Body_Type":"Hatch back",
    "Price":"7.11 Lakh",
    "Waiting_Period":"9 Weeks",
    "Transmission":"Manual",
    "Fuel_Type":"Petrol",
    "Length":"3845 cm",
    "Width":"1735 cm",
    "Height":"1530 cm",
    "Engine_CC":"1197 ",
    "Mileage":"22.38 km/pl",
    "Boot_Space":"268 L",
    "Seats":"5",
    "Airbags":"2",
    "Camera":"No",
    "HeadLight":"Halogen",
    "Rating":"4.4",
    "image":"C:\\Users\\Dell\\Downloads\\swift.jpg"
}]




