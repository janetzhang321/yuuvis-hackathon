document.getElementById('my-form').addEventListener("submit", function (e) {
    e.preventDefault();
    let searchResult = document.querySelector(".search-bar").value;
    
    document.querySelector(".button").addEventListener("click", () => {
        body.style.color = "yellow";
    })

    let query={
        "query": {
        "statement": "SELECT * FROM enaio:object where contains('"+searchResult+"')",
        "skipCount": 0,
        "maxItems": 50
        }
    }

    let myJSON = JSON.stringify(query);



    //return (myJSON)
});


function myEnterFunction() {
    element = document.getElementById("demo");
    element.style.backgroundColor = "{{ color }}";
};