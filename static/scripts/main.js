(() => {
    const map = L.map('map');
    map.setView([44.650627, -63.597140], 14);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    const getData = async () => {
        const res = await fetch("/api/get-data");
        const data = await res.json();

        console.log(data);
    }

    getData();
})();