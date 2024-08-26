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
}

// const getYearValue = () => {
//     const uiYear = document.getElementById('uiYear');
//     const selectedYear = parseInt(uiYear.value, 10); // Get the selected year as an integer
//     const currentYear = new Date().getFullYear(); // Get the current year

//     if (!isNaN(selectedYear)) {
//         return currentYear - selectedYear; // Return the difference
//     }
//     return null; // Return null if no valid year is selected
// };

const checkLength = () => {
    const kmDrivenInput = document.getElementById('km_driven');
    const maxLength = 8;

    if (kmDrivenInput.value.length > maxLength) {
        kmDrivenInput.value = kmDrivenInput.value.slice(0, maxLength);
        alert('KM Driven cannot exceed 8 digits.')
    }
}

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
 }

const onClickedEstimatePrice = () => {
    console.log('Estimate button clicked!');
}

window.onload = onPageLoad;
