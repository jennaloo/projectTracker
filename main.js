document.getElementById('submitBtn').addEventListener('click', function() {
    var status = document.getElementById('status').value;

    fetch('/data.json')
        .then(response => response.json())
        .then(data => {
            var filteredProjects = data.filter(project => project.status_id.toString() === status);

            var output = document.getElementById('output');
            output.innerHTML = '';

            filteredProjects.forEach(project => {
                var projectName = project.title;
                var projectDescription = project.description;

                var projectDiv = document.createElement('div');
                projectDiv.classList.add('project');
                projectDiv.innerHTML = '<h3>' + projectName + '</h3><p>' + projectDescription + '</p>';

                output.appendChild(projectDiv);
            });
        })
        .catch(error => console.error(error));
});
