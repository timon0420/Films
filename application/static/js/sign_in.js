const create_image = () => {
    let image = document.createElement('img');
    image.classList.add("show_password")
    image.src = "static/images/show.png"
    let input_box = document.querySelector("#input_box");
    input_box.appendChild(image);
}
const show_password = () => {
    let type = 'password';
    let input_password = document.querySelector("#input_password");
    create_image();
    let button = document.querySelector('.show_password');
    button.addEventListener('click', () => {
        if (type == 'password') {
            type = 'text';
            input_password.type = type;
            button.src = "static/images/hide.png";
        }
        else if (type == 'text') {
            type = 'password';
            input_password.type = type;
            button.src = "static/images/show.png";
        }
    })
}
show_password();