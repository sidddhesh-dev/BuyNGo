document.addEventListener("DOMContentLoaded", function () {
    
    const btn = document.getElementById("categoryBtn");
    const list = document.getElementById("categoryList");

    btn.addEventListener("click", function (e) {
        e.preventDefault();

        // Toggle show/hide
        if (list.style.display === "none") {
            list.style.display = "block";
        } else {
            list.style.display = "none";
        }
    });

});
