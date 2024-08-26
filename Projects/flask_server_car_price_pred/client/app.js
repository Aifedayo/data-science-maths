const onPageLoad = async () => {
    const url = 'http://localhost:5000/car_brand'
    try {
        const response = await fetch(url);
        const data = await response.json();
        console.log('Got response for car brands: ', data);

        if (data) {
            const car_brands = data.car_brands;
            const uiCarBrands = document.getElementById('uiCarBrands');
            uiCarBrands.innerHTML = '';

            car_brands.forEach(car_brand => {
                const opt = new Option(car_brand);
                uiCarBrands.appendChild(opt);
            });
        }
    } catch (error) {
        console.error('Error: ', error)
    }
}

window.onload = onPageLoad;
