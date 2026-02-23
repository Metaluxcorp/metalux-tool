import streamlit as st

st.set_page_config(page_title="Metalux Estimate/Invoice Generator", page_icon="🏗️")

st.title("🏗️ Metalux Estimate/Invoice Generator")
st.markdown("Use this to generate uniform invoice descriptions. Fill in the fields and copy the result.")

# Sidebar for Project Selection
project_type = st.sidebar.selectbox(
    "Select Project Type",
    ["Structural Steel", "Misc Metals", "Composite Decking"]
)

# Logic for different projects
if project_type == "Structural Steel":
    st.header("Structural Steel Details")
    
    # Using three columns for a tighter layout
    row1_col1, row1_col2, row1_col3 = st.columns(3)
    with row1_col1:
        columns = st.number_input("Columns", min_value=0, step=1)
    with row1_col2:
        beams = st.number_input("Beams", min_value=0, step=1)
    with row1_col3:
        channels = st.number_input("Channels", min_value=0, step=1)
        
    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        embeds = st.number_input("Embeds", min_value=0, step=1)
        plans = st.text_input("Plan Reference (e.g. S-101)")
    with row2_col2:
        finish = st.selectbox("Finish Type", ["Metalux Gray Primer", "Galvanized", "Raw Steel", "Powder Coated"])

    # Formatting the output with the new Channels line
    description = f"""PROJECT SCOPE: Custom Structural Steel Fabrication
--------------------------------------------------
COMPONENTS: ({columns}) Columns | ({beams}) Beams 
            ({channels}) Channels | ({embeds}) Embeds
MATERIAL: Grade A36 Structural Steel
FINISH: {finish}
REF: Per Blueprints / Plan Page(s): {plans if plans else "N/A"}"""
elif project_type == "Misc Metals":
    st.header("Misc Metals Details")
    col1, col2 = st.columns(2)
    with col1:
        railing = st.number_input("Linear Ft. of Railing", min_value=0)
        brackets = st.number_input("Number of Brackets", min_value=0)
    with col2:
        style = st.text_input("Railing Style")
        finish = st.selectbox("Finish", ["Powder Coated", "Primed", "Raw"])

    description = f"""PROJECT SCOPE: Custom Miscellaneous Metals
--------------------------------------------------
ITEMS: ({railing}) LF of {style if style else "Custom"} Railing | ({brackets}) Brackets
FABRICATION: All welds ground smooth / Industrial Grade
FINISH: {finish}
INSTALL: Included as per proposal"""

elif project_type == "Composite Decking":
    st.header("Decking Details")
    size = st.text_input("Footprint (e.g. 20x20)")
    color = st.text_input("Board Brand/Color")
    railing_included = st.checkbox("Include Railing?")
    
    rail_status = "Included" if railing_included else "Not Included"
    
    description = f"""PROJECT SCOPE: Composite Wood Deck Installation
--------------------------------------------------
FOOTPRINT: {size} Sq. Ft.
BOARD TYPE: {color}
DETAILS: Hidden Fasteners | Picture Frame Border
RAILING: {rail_status}"""

# Display and Copy Section
st.divider()
st.subheader("Final Description")
st.text_area("Copy this into QuickBooks:", value=description, height=200)

st.info("💡 Highlight the text above and press Ctrl+C (Cmd+C) to copy.")
