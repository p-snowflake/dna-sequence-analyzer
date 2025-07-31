import streamlit as st
import matplotlib.pyplot as plt

st.title("🧬 DNA Sequence Analyzer 🧬")
st.markdown("*A Simple Tool to analyze Nucleotide Count, Base Composition, GC/AT Ratio, Reverse Complement and Visualize the Results.*")


# Input from FASTA file or manual text
st.header("Input DNA Sequence")
st.write("You can either upload a FASTA file or type the sequence directly below.")
uploaded = st.file_uploader("Upload FASTA file", type=["fasta", "fa"])
sequence= ""

if uploaded:
    contents = uploaded.read().decode().splitlines()
    sequence = "".join(line.strip() for line in contents if not line.startswith(">")).upper()

else:
    sequence = st.text_input("Or enter DNA sequence:").upper()


if sequence:
    # Input validation
    if not all(base in {'A', 'T', 'G', 'C'} for base in sequence):
        st.error("Invalid Input! Please enter a sequence containing only A, T, G, and C.")
    else:
        # Count of nucleotides
        A_count = sequence.count('A')
        T_count = sequence.count('T')
        G_count = sequence.count('G')
        C_count = sequence.count('C')
        total_length = len(sequence)

        # Basic Summary
        st.header("Sequence Summary")
        st.write("Total Number of Bases:", total_length)
        st.write("Nucleotide Counts: A :", A_count, " | T :", T_count, " | G :", G_count, " | C :", C_count)

        # Sequence Composition
        st.header("Composition Analysis")
        at = ((A_count + T_count) / total_length) * 100
        gc = ((G_count + C_count) / total_length) * 100

        st.write(f"AT Content: {at:.2f}%")
        st.write(f"GC Content: {gc:.2f}%")

        # GC/AT Ratio
        if at > 0:
            gc_at_ratio = gc / at
            st.write(f"GC/AT Ratio: {gc_at_ratio:.2f}")
        else:
            st.write("GC/AT Ratio: Cannot compute as AT content is zero.")


        # Richness Message
        if at > gc:
            st.info("Sequence is AT rich.")
        elif gc > at:
            st.info("Sequence is GC rich.")
        else:
            st.info("Sequence has balanced AT and GC content.")

        # Reverse Complement
        st.header("Reverse Complement")
        complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        rev_comp = ''.join(complement[base] for base in reversed(sequence))
        
        st.text_area("Reverse Complement", value=rev_comp, height=100)


        if sequence == rev_comp:
            st.info("This sequence is a Palindrome!")
        else:
            st.info("This sequence is not a Palindrome.")

        # Visualizations
        st.header("Nucleotide Composition Visualizations")
        colors = ['coral', 'lightseagreen', 'violet', 'gold']
        labels = ['A', 'T', 'G', 'C']
        values = [A_count, T_count, G_count, C_count]

        # Side-by-side layout for Pie and Bar chart
        col1, col2 = st.columns(2)

        with col1:
            fig1, ax1 = plt.subplots()
            ax1.pie(values, labels=labels, colors=colors, startangle=90, autopct='%1.1f%%')
            ax1.set_title("Nucleotide Composition - Pie Chart")
            ax1.axis('equal')
            st.pyplot(fig1)

        with col2:
            fig2, ax2 = plt.subplots()
            ax2.bar(labels, values, color=colors)
            ax2.set_title("Nucleotide Counts - Bar Chart")
            ax2.set_xlabel("Nucleotide")
            ax2.set_ylabel("Count")
            ax2.grid(axis='y')
            st.pyplot(fig2)
