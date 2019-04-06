document.getElementById('my-form').addEventListener("submit", function (e) {
    e.preventDefault();
    let searchResult = document.querySelector(".search-bar").value;
    return (searchResult)
});