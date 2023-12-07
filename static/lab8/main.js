function fillCourseList() {
    fetch('/lab8/api/courses/')
    .then(funtion (data) {
        return data.json();
    })
    .then(funtion (courses) {
        let tbody= document.getElementById('course-list');
        tbody.innerHTML ='';
        for( let i = 0; i<courses.length; i++) {
            tr=document.createElement('tr');

            let tdName= document.createElement('td');
            tdName.innerText= courses[i].name;

            let tdVideos= document.createElement('td');
            tdVideos.innerText= courses[i].videos;

            let tdPrice= document.createElement('td');
            tdPrice.innerText= courses[i].price || 'бесплатно';

            let editButton= document.createElement('button');
            editButton.innerHTML= 'редактировать';

            let delButton= document.createElement('button');
            editButton.innerHTML= 'удалить';

            let tdActions= document.createElement('td');
            tdActions.append(editButton);
            tdActions.append(delButton);
            

            tr.append(tdName);
            tr.append(tdVideos);
            tr.append(tdPrice);
            tr.append(tdActions);

            tbody.append(tr)
        }
    })
}

