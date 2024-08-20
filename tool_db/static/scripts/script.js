document.addEventListener('DOMContentLoaded', function() {
    let select = document.querySelectorAll('select');
    M.FormSelect.init(select);

    let modal = document.querySelectorAll('.modal');
    M.Modal.init(modal);
  });

  document.getElementById('register_form').addEventListener('submit', function(event) {
    const password = document.getElementById('password').value;
    const passwordConfirm = document.getElementById('password_confirm').value;
    
    if (password !== passwordConfirm) {
        event.preventDefault(); // Prevent form submission
        alert('Passwords do not match!');
    }
});