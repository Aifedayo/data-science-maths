document.addEventListener('DOMContentLoaded', function () {
    const manufacturerSelect = document.getElementById('manufacturer');
    const modelSelect = document.getElementById('model');
    const categorySelect = document.getElementById('category');
    const colorSelect = document.getElementById('color');
    const driveWheelsSelect = document.getElementById('drive_wheels');
    const prodYearSelect = document.getElementById('prod_year');

    

    // Populate production years
    for (let year = 1999; year <= 2100; year++) {
        let option = document.createElement('option');
        option.value = year;
        option.textContent = year;
        prodYearSelect.appendChild(option);
    }

    // Fetch data and populate dropdowns (mocked API calls)
    fetchManufacturers();
    fetchCategories();
    fetchColors();
    fetchDriveWheels();

    manufacturerSelect.addEventListener('change', function () {
        fetchModels(this.value);
    });

    async function fetchManufacturers() {
        const url = 'http://localhost:5000/object/manufacturers'
        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error('Netork response was not ok');
            }
            const data = await response.json();
            if (data && data.objects) {
                let manufacturers = data.objects;

                manufacturers.sort((a, b) => a.localeCompare(b));

                manufacturerSelect.innerHTML = '<option value="">Select Manufacturer</option>';
                populateSelect(manufacturerSelect, manufacturers);
                let otherOption = document.createElement('option');
                otherOption.value = "other";
                otherOption.textContent = "Other";
                manufacturerSelect.appendChild(otherOption);
            }
            
        } catch (error) {
            console.error('Error: ', error)
        }
    }

    async function fetchModels(manufacturer) {
        const url = 'http://localhost:5000/manufacturer/' + manufacturer
        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error('Network response was not OK!')
            }
            const data = await response.json()
            if (data && data[manufacturer]) {
                let models = data[manufacturer]

                models.sort((a,b) => a.localeCompare(b));

                modelSelect.innerHTML = '<option value="">Select Model</option>';
                populateSelect(modelSelect, models || []);
                modelSelect.innerHTML += '<option value="other">Other</option>';
            }
        } catch (error) {
            console.error('Error: ', error)
        }
    }

    function fetchCategories() {
        // Mocked API call
        const categories = ['Sedan', 'SUV', 'Coupe', 'Convertible'];
        populateSelect(categorySelect, categories);
    }

    function fetchColors() {
        // Mocked API call
        const colors = ['Red', 'Blue', 'Black', 'White'];
        populateSelect(colorSelect, colors);
    }

    function fetchDriveWheels() {
        // Mocked API call
        const driveWheels = ['FWD', 'RWD', 'AWD', '4WD'];
        populateSelect(driveWheelsSelect, driveWheels);
    }

    function populateSelect(selectElement, options) {
        options.forEach(option => {
            let opt = document.createElement('option');
            opt.value = option.toLowerCase();
            opt.textContent = option;
            selectElement.appendChild(opt);
        });
    }
});
