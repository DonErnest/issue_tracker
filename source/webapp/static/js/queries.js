function getToken () {
    return $.ajax({
        url: 'http://localhost:8000/api/v1/login/',
        method: 'post',
        data: JSON.stringify({username: 'nurik', password: 'presidentforever'}),
        dataType: 'json',
        contentType: 'application/json',
        success: function(response, status){
            localStorage.setItem('apiToken', response.token);
            performRequests()
        },
        error: function(response, status){console.log(response);}
    });
}

function checkIfToken() {
    return new Promise(function(resolve, reject) {
        let token = localStorage.getItem('apiToken');
        if (token) {
            console.log('Есть токен');
            performRequests();
        } else {
            console.log('Нет токена, пошли получать')
            getToken();
        }
    })
}

function viewAllProjects () {
    $.ajax({
        url: 'http://localhost:8000/api/v1/projects/',
        method: 'get',
        headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
        data: JSON.stringify({username: 'admin', password: 'admin'}),
        dataType: 'json',
        contentType: 'application/json',
        success: function(response, status){console.log(response);},
        error: function(response, status){console.log(response);}
    });
}

function viewAllTasks() {
    $.ajax({
        url: 'http://localhost:8000/api/v1/tasks/',
        method: 'get',
        headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
        data: JSON.stringify({username: 'admin', password: 'admin'}),
        dataType: 'json',
        contentType: 'application/json',
        success: function(response, status){console.log(response);},
        error: function(response, status){console.log(response);}
    });
}


function getTasksforProject () {
    $.ajax({
        url: 'http://localhost:8000/api/v1/tasks/?project=3',
        method: 'get',
        headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
        data: JSON.stringify({username: 'admin', password: 'admin'}),
        dataType: 'json',
        contentType: 'application/json',
        success: function(response, status){console.log(response);},
        error: function(response, status){console.log(response);}
    });
}

function addTaskforProject() {
    $.ajax({
        url: 'http://localhost:8000/api/v1/tasks/',
        method: 'post',
        headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
        data: JSON.stringify({
            "summary": "Провести ряд репрессий",
            "description": "На всякий случай, надо провести ряд репрессий, чтобы обеспечить стабильность",
            "status":5,
            "type": 1,
            "assigned_to": 22,
            "created_by": 15,
            "project": 17
        }),
        dataType: 'json',
        contentType: 'application/json',
        success: function(response, status){console.log(response);},
        error: function(response, status){console.log(response);}
    });
}

function deleteSelectedTask() {
    $.ajax({
        url: 'http://localhost:8000/api/v1/tasks/82/',
        method: 'delete',
        headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
        dataType: 'json',
        contentType: 'application/json',
        success: function(response, status){console.log('Удаление прошло успешно!')},
        error: function(response, status){console.log(response);}
    });
}

function performRequests() {
    viewAllTasks();
    viewAllProjects();
    getTasksforProject();
    addTaskforProject();
    deleteSelectedTask();
}

checkIfToken();



// Аякс запрос на logout  и удаление токена из локального хранилища
//
// $.ajax({
//         url: 'http://localhost:8000/api/v1/logout/',
//         method: 'post',
//         headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
//         dataType: 'json',
//         contentType: 'application/json',
//         success: function(response, status){console.log(response)},
//         error: function(response, status){console.log(response);}
//     });
// localStorage.removeItem('apiToken');
//