import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.title("Graphing Test!")
st.write("I am just testing out Streamlit and also deploying to GitHub Pages. Don't mind this, just a test.")

# Frequency and Amplitude sliders
frequency = st.slider("Select frequency", 1, 20)
amplitude = st.slider("Select amplitude", 0.1, 2.0)
# Time value
time = np.linspace(0, 1, 1000)
# y value
y = amplitude * np.sin(2 * np.pi * frequency * time)
# Checkbox for noise
noise = st.checkbox("Add noise") 
if noise:
    st.write("Noise will be added to the signal.")
    y += np.random.rand(len(time)) * 0.2

# Create figure and axis
fig, ax = plt.subplots()
# Draw
ax.plot(time, y)
ax.set_xlabel("Time [s]")
ax.set_ylabel("Amplitude")
ax.set_title("y(t) = A * sin(2πft)")
# Show plot in Streamlit
st.pyplot(fig)