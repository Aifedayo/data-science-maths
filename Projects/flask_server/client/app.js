const getBathValue = () => {
    const uiBathrooms = document.getElementsByName("uiBathrooms");
    for(let i=0; i < uiBathrooms.length; i++) {
      if(uiBathrooms[i].checked) {
          return i+1;
      }
    }
    return -1; // Invalid Value
};
  
const getBHKValue = () => {
    const uiBHK = document.getElementsByName("uiBHK");
    for(let i=0; i < uiBHK.length; i++) {
      if(uiBHK[i].checked) {
          return i+1;
      }
    }
    return -1; // Invalid Value
  }
  
const onClickedEstimatePrice = async () => {
    console.log("Estimate price button clicked");

    const sqft = document.getElementById("uiSqft");
    const BHK = getBHKValue();
    const bathrooms = getBathValue();
    const location = document.getElementById("uiLocations");
    const estPrice = document.getElementById("uiEstimatedPrice");
  
    // const url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
    const url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

    const formData = new URLSearchParams({
        total_sqft: parseFloat(sqft.value),
        BHK: BHK,
        bath: bathrooms,
        location: location.value
      }).toString();
      try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: formData
        });
        const data = await response.json();
        estPrice.innerHTML = `<h2>${data.estimated_price} Lakh</h2>`;
        console.log(data.estimated_price);
    } catch (error) {
        console.error('Error:', error);
    }
};
  
const onPageLoad = async () => {
    console.log( "document loaded" );
    // const url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
    const url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    try {
        const response = await fetch(url);
        const data = await response.json();
        console.log('Got response for location names request!', data);

        if (data) {
            const locations = data.locations;
            const uiLocations = document.getElementById('uiLocations');
            uiLocations.innerHTML = '';

            locations.forEach(location => {
                const opt = new Option(location);
                uiLocations.appendChild(opt);
            });
        }
    } catch (error) {
        console.error('Error: ', error)
    }
};
  
window.onload = onPageLoad;
