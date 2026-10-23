// загрузка пользователей
async function loadUsers() {
    let res = await fetch('/users/');
    let data = await res.json();

    let list = document.getElementById('users');
    list.innerHTML = '';

    data.forEach(u => {
        let li = document.createElement('li');
        li.textContent = u.name;
        list.appendChild(li);
    });
}

// добавление пользователя
async function addUser() {
    let name = document.getElementById('name').value;

    await fetch('/users/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({name: name})
    });

    loadUsers();
}

// загрузка постов
async function loadPosts() {
    let res = await fetch('/posts');
    let data = await res.json();

    let list = document.getElementById('posts');
    list.innerHTML = '';

    data.forEach(p => {
        let li = document.createElement('li');
        li.textContent = p.title;
        list.appendChild(li);
    });
}

// добавление поста
async function addPost() {
    let title = document.getElementById('title').value;

    await fetch('/posts', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({title: title})
    });

    loadPosts();
}

// при загрузке страницы
loadUsers();
loadPosts();