import streamlit as st
import random

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

st.set_option('deprecation.showPyplotGlobalUse', False)

def run_raffle(start_num, end_num, num_draws, with_replacement):
    ticket_pool = list(range(start_num, end_num + 1))
    results = []

    for draw_count in range(1, num_draws + 1):
        winning_ticket = random.choice(ticket_pool)
        results.append((draw_count, winning_ticket))

        if not with_replacement:
            ticket_pool.remove(winning_ticket)

    return results

st.title("Raffle App")
st.write("By: [Alexis Vera](mailto:alexisvera@gmail.com)")

# Instructions with Expander
expander = st.expander("Instructions")
expander.write("""
**How to use this Raffle App:**

1. **Enter Ticket Range:** Input the starting and ending ticket numbers for your raffle.

2. **Number of Draws:** Decide on how many winning tickets you want to draw.

3. **Allow Reposition:** Check this box if the same ticket can win multiple prizes. Otherwise, leave it unchecked.

4. **Execute Raffle:** Press the "Execute Raffle" button to run the raffle.

5. **Results:** The table will display the draw number (prize) and the winning ticket number.
""")

# User Inputs
start_ticket = st.number_input("Starting Ticket Number", min_value=0)
end_ticket = st.number_input("Ending Ticket Number", min_value=start_ticket)
num_draws = st.number_input("Number of Draws", min_value=1)
with_replacement = st.checkbox("Allow Reposition (Same Ticket Can Win Multiple Times)")

# Execute Raffle Button
if st.button("Execute Raffle"):
    if num_draws > 0: 
        results = run_raffle(start_ticket, end_ticket, num_draws, with_replacement)

        # Display Results Table 
        if results:
            st.write("### Raffle Results")
            st.write("Draw (Prize) | Ticket No. (Winner)") 
            for draw, ticket in results:
                st.write(f"{draw} | {ticket}")
            st.balloons()  

    else:
        st.warning("Unable to execute the raffle. Please, enter the number of draws for the raffle.")
