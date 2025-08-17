import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Normal Distribution: Empirical Rule")
st.title("Normal Distribution & the 68-95-99.7 Rule")

st.markdown("""
**Empirical Rule:**  
For a normal distribution:  
- ~68% of data within 1 standard deviation  
- ~95% within 2 standard deviations  
- ~99.7% within 3 standard deviations
""")

mean = st.slider("Mean", -10.0, 10.0, 0.0)
std = st.slider("Standard Deviation", 0.5, 5.0, 1.0)

data = np.random.normal(loc=mean, scale=std, size=1000)

fig, ax = plt.subplots()
ax.hist(data, bins=30, color='lightblue', edgecolor='black', alpha=0.7)

for i, color in zip([1, 2, 3], ['green', 'yellow', 'red']):
    ax.axvspan(mean-i*std, mean+i*std, alpha=0.2, color=color)
    ax.text(mean+i*std, ax.get_ylim()[1]*0.9, f"±{i} std", color=color)

st.pyplot(fig)

within_1 = np.mean((data > mean-std) & (data < mean+std))
within_2 = np.mean((data > mean-2*std) & (data < mean+2*std))
within_3 = np.mean((data > mean-3*std) & (data < mean+3*std))

st.write(f"Proportion within 1 std: {within_1:.2f}")
st.write(f"Proportion within 2 std: {within_2:.2f}")
st.write(f"Proportion within 3 std: {within_3:.3f}")
