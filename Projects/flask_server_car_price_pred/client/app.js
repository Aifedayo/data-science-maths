const checkLength = () => {
    const kmDrivenInput = document.getElementById('km_driven');
    const maxLength = 8;

    if (kmDrivenInput.value.length > maxLength) {
        kmDrivenInput.value = kmDrivenInput.value.slice(0, maxLength);
        alert('KM Driven cannot exceed 8 digits.')
    }
};

 const validateForm = () => {
    const form = document.getElementById('carForm');
    const requiredFields = form.querySelectorAll('[required]');

    for (let field in requiredFields) {
        if (!field.value.trim()) {
            field.focus();
            return false;
        }
    }
    return true;
};

const onClickedEstimatePrice =  async () => {
    console.log('Estimate button clicked!');
    const currentYear = new Date().getFullYear();
    const url = "http://localhost:5000/predict_car_price";

// Collect values from the form elements
    const name = document.getElementById('uiCarBrands').value;
    const year = parseInt(document.getElementById('uiYear').value, 10);
    const km_driven = parseInt(document.getElementById('km_driven').value, 10);
    const transmission = document.querySelector('input[name="transmission"]:checked')?.value || '';
    const owner = document.querySelector('input[name="owner"]:checked')?.value || '';
    const seats = Array.from(document.querySelectorAll('input[name="seat"]:checked')).map(el => el.value);
    const mileage = parseFloat(document.getElementById('mileage').value) || 0;
    const engine = parseInt(document.getElementById('engine').value, 10) || 0;
    const seller_type = Array.from(document.querySelectorAll('input[name="seller_type"]:checked')).map(el => el.value);
    const fuel = Array.from(document.querySelectorAll('input[name="fuel"]:checked')).map(el => el.value);

    const estimatedPrice = document.getElementById('estimatedPrice')
    // Calculate year difference
    const yearDifference = year ? currentYear - year : '';

    const formData = new URLSearchParams({
        name: name,
        year: yearDifference,
        km_driven: km_driven,
        transmission: transmission,
        owner: owner,
        seats: seats.join(','), // Convert array to comma-separated string
        mileage: mileage,
        engine: engine,
        seller_type: seller_type.join(','), // Convert array to comma-separated string
        fuel: fuel.join(',') // Convert array to comma-separated string
    }).toString();
    console.log(formData)
    try {
        const response = await fetch (url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: formData
        });
        const data = await response.json();
        estimatedPrice.innerHTML = data.estimated_price
    } catch (error) {
        console.error('Error: ', error)
    }
};

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
            const defaultOption = new Option('Choose a Car Brand', "");
            defaultOption.disabled = true;
            defaultOption.selected = true;
            uiCarBrands.appendChild(defaultOption);

            car_brands.forEach(car_brand => {
                const opt = new Option(car_brand);
                uiCarBrands.appendChild(opt);
            });
        }
    } catch (error) {
        console.error('Error: ', error)
    }
};

window.onload = onPageLoad;
