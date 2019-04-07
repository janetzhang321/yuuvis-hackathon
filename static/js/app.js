document.getElementById('my-form').addEventListener("submit", function (e) {
    e.preventDefault();
    let searchResult = document.querySelector(".search-bar").value;
    //console.log(searchResult)

    let query={
        "query": {
        "statement": "SELECT * FROM enaio:object where contains('"+searchResult+"')",
        "skipCount": 0,
        "maxItems": 50
        }
    }

    let myJSON = JSON.stringify(query);

    console.log(myJSON)

    function myEnterFunction() {
        element = document.getElementById("demo");
        element.style.backgroundColor = "{{ d }}";
    }

    //return (myJSON)
});