(() => {

    const map = L.map('map');
    map.setView([44.650627, -63.597140], 7);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    const projectIcon = L.icon({
        iconUrl: '/static/images/project-management.png',
        iconSize: [25, 25]
    });

    const foodIcon = L.icon({
        iconUrl: '/static/images/diet.png',
        iconSize: [25, 25]
    });

    const renderData = async () => {
        const res = await fetch("/api/get-data");
        const data = await res.json();

        console.log(data);


        data.projects.forEach(project => {

            let marker = L.marker([project.Latitude, project.Longitude], {icon: projectIcon})
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

        data.food_banks.forEach(foodBank => {

            let marker = L.marker([foodBank.Lat, foodBank.Lng], {icon: foodIcon})
            marker.bindPopup(
                `
                <p>Org Name: ${foodBank.Name}</p>
                <p>Address: ${foodBank.Address}</p>
                <p>Email: ${foodBank.Email}</p>
                <p>Phone Number: ${foodBank["Phone Number"]}</p>
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