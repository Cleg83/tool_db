document.addEventListener('DOMContentLoaded', function() {
    let select = document.querySelectorAll('select');
    M.FormSelect.init(select);

    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    let modal = document.querySelectorAll('.modal');
    M.Modal.init(modal);

  });