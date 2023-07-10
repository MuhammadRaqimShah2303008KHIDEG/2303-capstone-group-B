import uvicorn
from fastapi import FastAPI

from src.online_vs_inperson_comparison_service.config import PRICES_URL
from src.online_vs_inperson_comparison_service.functions import (
    calculate_savings,
    get_data_from_url,
    get_distance_time_from_tomtom,
)

app = FastAPI()


@app.get("/")
def api_working() -> str:
    return "Api is working, Please give the patient_id and councilor_id after /"


@app.get("/{patient_id}/{councillor_id}")
def get_data(
    patient_id: int,  # pylint: disable=unused-argument
    councillor_id: int,  # pylint: disable=unused-argument
) -> dict:
    """
    The function calls the get_patient_data function and get_councillor_data, passing patient_id and councillor_id as
    an argument. It retrieves the patient's location and councillor's location information by invoking the
    get_patient_data function and get_councillor_data respectively. From patient's location and councillor's location
    retriving latitude and longitude and passiing it to function get_distance_time_from_tomtom which retrives time
    and distance

    Parameters:
        patient_id (int): patient id to be used to fetch patient's location.
        councillor_id (int): councillor id to be used to fetch councillor's location.

    Returns:
        Dict: values containing for distance in km , total_cost_saved , currency, co2 and methane saved.
    """

    # TODO: the code below is commented out because the dummy data does not work correctly. Hardcoding example locations
    # for now, once we can query real users data this should be changed.
    # # Get patient data
    # patient_location = get_location_data(patient_id, True)
    # # Get councillor data
    # councillor_location = get_location_data(councillor_id, False)

    # giving dummy data because above data is not providing the correct data for route api
    patient_lat = 24.853933630083414  # patient_location["latitude"]
    patient_long = 67.01242544738403  # patient_location["longitude"]
    councillor_lat = 24.85208510663253  # councillor_location["latitude"]
    councillor_long = 67.01200372652839  # councillor_location["longitude"]

    # getting distance and time
    ditstance_time = get_distance_time_from_tomtom(
        patient_lat,
        patient_long,
        councillor_lat,
        councillor_long,
    )

    # getting fuel price and currency  from fuel-price url
    data_from_fuel_service = get_data_from_url(
        f"{PRICES_URL}{patient_lat}/{patient_long}"
    )
    currency = data_from_fuel_service["currency"]
    fuel_price = data_from_fuel_service["fuel_price"]

    calculated_result = calculate_savings(ditstance_time["distance"], float(fuel_price))
    total_cost_saved = calculated_result["total_cost"]
    co2_saved = calculated_result["co2_saved"]
    methane_saved = calculated_result["methane_saved"]
    return {
        "total_time_saved_in_mins": ditstance_time["time"],
        "total_cost_saved": total_cost_saved,
        "currency": currency,
        "co2_saved": co2_saved,
        "methane_saved": methane_saved,
    }


if __name__ == "__main__":
    # Run the FastAPI application
    uvicorn.run(app="main:app", reload=True, host="0.0.0.0", port=8000)
