import streamlit as st
from time import sleep, time


pomodoro_duration = 25
break_duration = 5
long_break_after = 4
current_state = "idle"
start_time = 0


st.title("Pomodoro Timer")


if current_state == "pomodoro":
    remaining_time = int(pomodoro_duration - (time() - start_time))
    st.subheader(f"Pomodoro in progress... {remaining_time} seconds remaining")
elif current_state == "break":
    remaining_time = int(break_duration - (time() - start_time))
    st.subheader(f"Short break... {remaining_time} seconds remaining")
elif current_state == "long_break":
    remaining_time = int(long_break_after * pomodoro_duration + break_duration - (time() - start_time))
    st.subheader(f"Long break... {remaining_time} seconds remaining")
else:
    st.subheader("Ready to start your next pomodoro?")


if current_state == "idle":
    start_button = st.button("Start Pomodoro")
    if start_button:
        current_state = "pomodoro"
        start_time = time()
elif current_state in ("pomodoro", "break"):
    stop_button = st.button("Stop Timer")
    if stop_button:
        current_state = "idle"
        pomodoro_duration = 25  

if current_state in ("pomodoro", "break", "long_break"):
    remaining_time = int(pomodoro_duration - (time() - start_time))
    while remaining_time > 0:
        sleep(1)
        remaining_time -= 1
        st.subheader(f"{current_state}... {remaining_time} seconds remaining")

   
    if current_state == "pomodoro":
        if (long_break_after - 1) % 4 == 0:
            current_state = "long_break"
        else:
            current_state = "break"
        start_time = time()
    elif current_state == "break":
        current_state = "pomodoro"
        start_time = time()
    elif current_state == "long_break":
        current_state = "idle"

st.info("You can customize the timer durations and long break frequency in the code.")

