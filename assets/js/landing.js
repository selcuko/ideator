$ideaForm = document.getElementById('idea-form');
$ideaForm.onsubmit = (e) => {
    e.preventDefault();
    const fd = new FormData($ideaForm);
    fetch('', {
        method: 'POST',
        body: fd,
    }).then(response => {
        if (response.ok) location.href = response.url;
        else {
            input = document.getElementById('idea-submit');
            input.classList.add('error');
        }
    })
}