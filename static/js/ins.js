function showMore(){
    var pageCur = Number(document.getElementById("page-cur").value);
    var pageNum = Number(document.getElementById("page-num").value);
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
            document.getElementsByClassName("ins-container")[0].innerHTML += data;
            document.getElementById("page-cur").value = pageCur;
            if (pageCur == pageNum){
                document.getElementById("show-more").classList.add("disabled");
            }

            var numPages = document.getElementsByClassName("pagination")[0];
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

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('filter-form');
    const resultsDiv = document.getElementById('results');

    form.addEventListener('submit', function (e) {
        e.preventDefault(); // Забороняємо стандартне надсилання форми

        // Отримуємо значення селектора
        const formData = new FormData(form);
        const selectedType = formData.get('type');

        // Виконуємо AJAX-запит
        fetch(`/ins/?type=${encodeURIComponent(selectedType)}`, {
            headers: {
                'X-Requested-With': 'XMLHttpRequest' // Позначаємо AJAX-запит
            }
        })
        .then(response => {
            if (!response.ok) throw new Error('Помилка завантаження');
            return response.text(); // Очікуємо HTML
        })
        .then(data => {
            resultsDiv.innerHTML = data; // Оновлюємо контент
        })
        .catch(error => console.error('Помилка:', error));
    });
});
