function showMore_News(){
    var pageCur = Number(document.getElementById("page-cur-news").value);
    var pageNum = Number(document.getElementById("page-num-news").value);
    pageCur +=1
    fetch('?page=' + pageCur, {
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
        .then(response => {
            console.log(response)
            if (!response.ok) {
                throw new Error('Network response was not ok' + response.statusText);
            }
            return response.text()
        })
        .then(data => {
            document.getElementsByClassName("new-container")[0].innerHTML += data;
            document.getElementById("page-cur-news").value = pageCur;
            if (pageCur == pageNum){
                document.getElementById("show-more-news").classList.add("disabled");
            }

            var numPages = document.getElementById("pag-news");
            let ind = 0
            for (let nP of numPages.children) {
                nP.classList.remove("active");
                nP.classList.remove("disabled");
                if (pageCur == ind) {
                    nP.classList.add("disabled");
                }
                ind++;

            }

        })
        .catch(error => console.log('Error', error))
};