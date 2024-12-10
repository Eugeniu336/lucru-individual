import streamlit as st
import psutil
import matplotlib.pyplot as plt
import time

def get_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    free_memory = memory_info.available / (1024 ** 2)  # Convert to MB
    return cpu_usage, free_memory

st.title("System Monitor")

cpu_usages = []
free_memories = []

placeholder = st.empty()

while True:
    cpu_usage, free_memory = get_system_metrics()
    cpu_usages.append(cpu_usage)
    free_memories.append(free_memory)

    if len(cpu_usages) > 20:
        cpu_usages.pop(0)
        free_memories.pop(0)

    fig, ax = plt.subplots(2, 1, figsize=(10, 8))

    ax[0].plot(cpu_usages, label='CPU Usage (%)')
    ax[0].set_title('CPU Usage Over Time')
    ax[0].set_ylabel('CPU Usage (%)')
    ax[0].legend()

    ax[1].plot(free_memories, label='Free Memory (MB)', color='orange')
    ax[1].set_title('Free Memory Over Time')
    ax[1].set_ylabel('Free Memory (MB)')
    ax[1].legend()

    placeholder.pyplot(fig)
    time.sleep(0.2)