import streamlit as st
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt


def generate_quantum_random_number(bits=8):
    qc = QuantumCircuit(bits, bits)

    for i in range(bits):
        qc.h(i)

    qc.measure(range(bits), range(bits))

    simulator = AerSimulator()
    result = simulator.run(qc, shots=1).result()
    counts = result.get_counts()

    binary_number = list(counts.keys())[0]
    decimal_number = int(binary_number, 2)

    return binary_number, decimal_number


st.title("Quantum Random Number Generator")
st.write("This app generates random numbers using quantum superposition.")

bits = st.slider("Select number of qubits/bits", 1, 16, 8)

if st.button("Generate Quantum Random Number"):
    binary, decimal = generate_quantum_random_number(bits)

    st.subheader("Result")
    st.write("Binary:", binary)
    st.write("Decimal:", decimal)

    fig, ax = plt.subplots()
    ax.bar(["Decimal Output"], [decimal])
    ax.set_ylabel("Value")
    ax.set_title("Generated Quantum Random Number")
    st.pyplot(fig)