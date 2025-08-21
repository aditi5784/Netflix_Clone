// Accordion functionality :
const items = document.querySelectorAll(".accordion li");

items.forEach(item => {
    const label = item.querySelector("label");

    label.addEventListener("click", () => {
        // Close all other items :
        items.forEach(el => {
            if (el !== item) el.classList.remove("active");
        });

        // Toggle current item :
        item.classList.toggle("active");
    });
});

// Horizontal scroll functionality :
const scrollContainer = document.getElementById("scrollable");
const leftBtn = document.querySelector(".scroll-btn.left");
const rightBtn = document.querySelector(".scroll-btn.right");

function updateButtons() {
    // Show left button if scroll > 0 :
    leftBtn.style.display = scrollContainer.scrollLeft > 0 ? "block" : "none";

    // Show right button if more content available :
    rightBtn.style.display = scrollContainer.scrollLeft + scrollContainer.clientWidth < scrollContainer.scrollWidth ? "block" : "none";
}

// Listen to scroll events :
scrollContainer.addEventListener("scroll", updateButtons);

// Initial button state :
updateButtons();

// Button click events :
leftBtn.addEventListener("click", () => {
    scrollContainer.scrollBy({ left: -300, behavior: "smooth" });
});

rightBtn.addEventListener("click", () => {
    scrollContainer.scrollBy({ left: 300, behavior: "smooth" });
});
