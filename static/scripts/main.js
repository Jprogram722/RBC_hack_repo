(() => {

    // grab the radio buttons
    const radioBtn = document.querySelectorAll(".radio")

    // create a variable to store the data
    let data;

    // make the map
    const map = L.map('map');
    map.setView([44.650627, -63.597140], 7);

    // request the map server
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
    
    // create project icon
    const projectIcon = L.icon({
        iconUrl: '/static/images/project-management.png',
        iconSize: [25, 25]
    });

    // create food icon
    const foodIcon = L.icon({
        iconUrl: '/static/images/diet.png',
        iconSize: [25, 25]
    });

    const renderData = async () => {
        const numProjectContainer = document.querySelector("#num-proj");

        const res = await fetch("/api/get-data");
        data = await res.json();

        console.log(data.projects);

        numProjectContainer.textContent += ` ${data.projects.length}`

        data.projects.forEach(project => {

            let marker = L.marker([project.Latitude, project.Longitude], {icon: projectIcon})
            marker.bindPopup(
                `
                <p>Department Name: ${project.DepartmentName}</p>
                <p>Program Name: ${project.ProgramName}</p>
                <p>Program Status: ${project.ProjectStatus}</p>
                <p>Municipality: ${project.Municipality}</p>
                <p># Of Units: ${project.NumberOfUnits}
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

    for(let i = 0; i < radioBtn.length; i++) {

    }

    renderData();
})();