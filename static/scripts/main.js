(() => {
    const getData = async () => {
        const res = await fetch("/api/get-data");
        const data = await res.json();

        console.log(data);
    }

    getData();
})();