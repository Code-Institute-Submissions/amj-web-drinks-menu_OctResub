/* This validates the add_post form */

const post_form = document.getElementById('add_post_form');
const title = document.getElementById('id_title').value;
const messageBlock = document.getElementById('form_validation_message');

function errorMessage(message){
    e.preventDefault();
    const messageText = document.createTextNode(message);
    messageBlock.appendChild(messageText);
}

post_form.addEventListener('submit', (e) => {
    
    if (title.length < 6) {
        errorMessage('Your title is too short');
        e.preventDefault();
    }
});