document.addEventListener('DOMContentLoaded', function() {
    let select = document.querySelectorAll('select');
    M.FormSelect.init(select);

    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    let modal = document.querySelectorAll('.modal');
    M.Modal.init(modal);

  });

  function fetchRandomTool() {
    fetch('/random_tool')
      .then(response => response.json())
      .then(data => {
        if (data.error) {
          console.error(data.error);
          return;
        }

        // Update card content
        document.getElementById('tool-name').textContent = data.tool_name;
        document.getElementById('tool-description').textContent = data.tool_description;

        // Update videos
        let toolVideos = document.getElementById('tool-videos');
        toolVideos.innerHTML = '';
        if (data.tool_videos) {
          data.tool_videos.forEach(video => {
            let embedUrl = video.replace("watch?v=", "embed/");
            toolVideos.innerHTML += `<iframe width="426" height="240" src="${embedUrl}" frameborder="0" allowfullscreen></iframe>`;
          });
        }

        // Update links
        let toolLinks = document.getElementById('tool-links');
        toolLinks.innerHTML = '';
        if (data.tool_links) {
          data.tool_links.forEach(link => {
            toolLinks.innerHTML += `<span class="home-page-links"><a href="${link}" target="_blank">Buy here</a></span>`;
          });
        } 
      })
      .catch(error => console.error('Error fetching random tool:', error));
  }

  // Initial fetch
  fetchRandomTool();

  // Fetch new random tool every 7.5 seconds
  setInterval(fetchRandomTool, 7500);