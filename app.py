import streamlit as st
import n2yo

# Create a function to get the skew azimuth and elevation for a given satellite
def get_skew_azimuth_elevation(satellite_id):
  tle = n2yo.get_tle(satellite_id)
  skew_azimuth = n2yo.get_skew_azimuth(tle)
  elevation = n2yo.get_elevation(tle)
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
  
