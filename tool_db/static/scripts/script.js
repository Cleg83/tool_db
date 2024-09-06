document.addEventListener('DOMContentLoaded', function() {
  // Initialise components

  let modal = document.querySelectorAll('.modal');
  M.Modal.init(modal, {});

  let select = document.querySelectorAll('select');
  M.FormSelect.init(select);

  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);



  // Initial fetch
  if (document.body.classList.contains('home-page')) {
      fetchRandomTool();
      
      // Fetch new random tool every 10 seconds
      fetchInterval = setInterval(fetchRandomTool, 10000);
  }
});

function fetchRandomTool() {
  fetch('/random_tool')
    .then(response => response.json())
    .then(data => {
      if (data.error) {
        console.error(data.error);
        return;
      }

      // Get the random tool card
      const randomToolCard = document.getElementById('random-tool-card');
      if (randomToolCard) {
          // Apply fade-out effect before updating content
          randomToolCard.classList.add('fade-out');
          randomToolCard.classList.remove('show');

          setTimeout(() => {
              // Update tool name with a link to the tool's page
              const toolLink = `<a href="/tool/${data.tool_id}" class="home-card-link">${data.tool_name}</a>`;
              document.getElementById('tool-name').innerHTML = toolLink;

              document.getElementById('tool-description').textContent = data.tool_description;

              // Update Add to My Toolbox button
              let toolAction = document.getElementById('tool-action');
              if (data.is_authenticated) {
                // Construct the dynamic URL for the form action
                const addToToolboxUrl = `/add_to_my_toolbox/${data.tool_id}`;
                
                toolAction.innerHTML = `
                  <form action="${addToToolboxUrl}" method="post" class="home-toolbox">
                    <button type="submit" class="edit-small borderless-btn">
                      <i class="fa-solid fa-toolbox"></i>
                      <small class="small-icon-text">Add to My Toolbox</small>
                    </button>
                  </form>
                `;
              } else {
                toolAction.innerHTML = ''; // Clear if not authenticated
              }

              // Remove fade-out and reapply fade-in effect
              randomToolCard.classList.remove('fade-out');
              randomToolCard.classList.add('show');
          }, 250); 
      }
    })
    .catch(error => console.error('Error fetching random tool:', error));
}

window.addEventListener('beforeunload', function() {
  if (fetchInterval) {
      clearInterval(fetchInterval);
  }
});