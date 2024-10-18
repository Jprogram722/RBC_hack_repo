(() => {

    const map = L.map('map');
    map.setView([44.650627, -63.597140], 7);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    const renderData = async () => {
        const res = await fetch("/api/get-data");
        const data = await res.json();

        console.log(data);


        data.projects.forEach(project => {

            let marker = L.marker([project.Latitude, project.Longitude])
            marker.bindPopup(
                `
                <p>Department Name: ${project.DepartmentName}</p>
                <p>Program Name: ${project.ProgramName}</p>
                <p>Program Status: ${project.ProjectStatus}</p>
                <p>Municipality: ${project.Municipality}</p>
                `,
                {
                    maxWidth: 300
                }
            )
            marker.addTo(map)
        });  
    }

    renderData();
})();