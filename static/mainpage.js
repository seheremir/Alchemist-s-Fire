// Görsel Yolları
const images = [
    "{{ url_for('static', filename='carousel_images/aot.jpg') }}",
    "{{ url_for('static', filename='carousel_images/vinland_saga.jpeg') }}",
    "{{ url_for('static', filename='carousel_images/delicious-in-dungeon.png') }}",
    "{{ url_for('static', filename='carousel_images/berserk.png') }}"
];

// Görsel Bağlantıları
const links = [
    "https://www.crunchyroll.com/series/GR751KNZY/attack-on-titan?srsltid=AfmBOorDVUjttec7-8Jv7hIf3P_XL9Z-U6xrMHK79dtMMWmG1fO-wjO_", // Attack on Titan için link
    "https://www.crunchyroll.com/series/GEXH3WKK0/vinland-saga", // Vinland Saga için link
    "https://www.netflix.com/tr/title/81564899", // Delicious in Dungeon için link
    "https://www.crunchyroll.com/series/GYX04955R/berserk" // Berserk için link
];

// Carousel Track Element
const track = document.getElementById('carousel-track');

// Dinamik Olarak Resimleri Ekleyelim
images.forEach((src) => {
    const item = document.createElement('div');
    item.className = 'carousel-item';

    const img = document.createElement('img');
    img.src = src;
    img.alt = 'Carousel Image';

    item.appendChild(img);
    track.appendChild(item);
});

// Overlay Hemen İzle Butonu
const overlay = document.createElement('div');
overlay.className = 'carousel-overlay';
overlay.innerHTML = `<button class="watch-now" onclick="watchNow()">Hemen İzle</button>`;
document.querySelector('.carousel').appendChild(overlay);

// Carousel Mantığı
let currentSlide = 0;

function moveSlide(direction) {
    const totalSlides = images.length;
    currentSlide = (currentSlide + direction + totalSlides) % totalSlides;

    // Her bir slide için dönüşüm
    track.style.transform = `translateX(-${currentSlide * 100}%)`;
}

// Hemen İzle Butonu
function watchNow() {
    // Mevcut görsele göre doğru linke git
    window.location.href = links[currentSlide];
}

// Sidebar Açma/Kapatma
let isSidebarOpen = false;

function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    sidebar.style.left = isSidebarOpen ? '-250px' : '0px';
    isSidebarOpen = !isSidebarOpen;
}

document.addEventListener("DOMContentLoaded", () => {
    const posterContainer = document.getElementById("posterContainer");
    const scrollLeftButton = document.getElementById("scrollLeft");
    const scrollRightButton = document.getElementById("scrollRight");

    const scrollContainer = (direction) => {
        const scrollAmount = 700; // Her tıklamada 700px kaydır
        posterContainer.scrollBy({
            left: direction === "right" ? scrollAmount : -scrollAmount,
            behavior: "smooth",
        });
    };

    scrollLeftButton.addEventListener("click", () => scrollContainer("left"));
    scrollRightButton.addEventListener("click", () => scrollContainer("right"));
});

const posterContainer = document.getElementById('posterContainer');
const scrollLeftButton = document.getElementById('scrollLeft');
const scrollRightButton = document.getElementById('scrollRight');

// Scroll left function
scrollLeftButton.addEventListener('click', () => {
    posterContainer.scrollBy({
        left: -300, // Her tıklamada 300px sola kayar
        behavior: 'smooth'
    });
});

// Scroll right function
scrollRightButton.addEventListener('click', () => {
    posterContainer.scrollBy({
        left: 300, // Her tıklamada 300px sağa kayar
        behavior: 'smooth'
    });
});
