import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode

STREAMLIT_AGGRID_URL = "https://github.com/PablocFonseca/streamlit-aggrid"
st.set_page_config(
    layout="centered", page_icon="🖱️", page_title="Interactive table app"
)
st.title("🖱️Interactive table app")
def aggrid_interactive_table(df):
    options = GridOptionsBuilder.from_dataframe(
        df, enableRowGroup=True, enableValue=True, enablePivot=True
    )
    options.configure_side_bar()
    options.configure_selection("single")
    selection = AgGrid(
        df,
        enable_enterprise_modules=True,
        gridOptions=options.build(),
        theme="light",
        update_mode=GridUpdateMode.MODEL_CHANGED,
        allow_unsafe_jscode=True,
    )
    return selection
lookup_table = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv")
selection = aggrid_interactive_table(df=lookup_table)
if selection:
    st.write("You selected:")
    st.json(selection["selected_rows"])

st.write("## Code")

st.code(
    '''
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode

STREAMLIT_AGGRID_URL = "https://github.com/PablocFonseca/streamlit-aggrid"
st.set_page_config(
    layout="centered", page_icon="🖱️", page_title="Interactive table app"
)
st.title("🖱️Interactive table app")
def aggrid_interactive_table(df):
    options = GridOptionsBuilder.from_dataframe(
        df, enableRowGroup=True, enableValue=True, enablePivot=True
    )
    options.configure_side_bar()
    options.configure_selection("single")
    selection = AgGrid(
        df,
        enable_enterprise_modules=True,
        gridOptions=options.build(),
        theme="light",
        update_mode=GridUpdateMode.MODEL_CHANGED,
        allow_unsafe_jscode=True,
    )
    return selection
lookup_table = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv")
selection = aggrid_interactive_table(df=lookup_table)
if selection:
    st.write("You selected:")
    st.json(selection["selected_rows"])
''',
    "python",
)