import streamlit as st
import n2yo

# Create a function to get the skew azimuth and elevation for a given satellite
def get_skew_azimuth_elevation(satellite_id):
  skew_azimuth = n2yo.tle(satellite_id).get_skew_azimuth()
  elevation = n2yo.tle(satellite_id).get_elevation()
  return skew_azimuth, elevation

# Create a Streamlit app
st.title("Satellite Tracker")

# Get the satellite ID from the user
satellite_id = st.text_input("Enter the satellite ID")

# Get the skew azimuth and elevation for the satellite
skew_azimuth, elevation = get_skew_azimuth_elevation(satellite_id)

# Display the skew azimuth and elevation to the user
st.write("The skew azimuth is {} degrees.".format(skew_azimuth))
st.write("The elevation is {} degrees.".format(elevation))

