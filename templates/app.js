window.addEventListener("load", function () {
    document.getElementById('my-form').addEventListener("submit", function (e) {
        e.preventDefault(); 
        let searchResult = document.querySelector(".search-bar").value;
    return(
    {
        “query”: {
        “statement”: “SELECT * FROM enaio:object where contains("'" + "'")“,
        “skipCount”: 0,
        “maxItems”: 50
        }
    }
        )
    });
});