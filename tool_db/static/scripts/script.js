document.addEventListener('DOMContentLoaded', function() {
    let select = document.querySelectorAll('select');
    M.FormSelect.init(select);

    let modal = document.querySelectorAll('.modal');
    M.Modal.init(modal);
  });