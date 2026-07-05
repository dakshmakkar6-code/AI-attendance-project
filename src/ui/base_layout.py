import streamlit as st


def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: #5865F2 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }

                .stApp div[data-testid="stColumn"] h2 {
                    color: black !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: #E0E3FF !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                

            /* Force light mode - override dark mode */
            .stApp, .stApp * {
                color-scheme: light !important;
            }

            p, li {
                color: #333333 !important;
            }

            button * {
                color: white !important;
            }



            /* Selectbox dropdown */
            div[data-baseweb="popover"],
            div[data-baseweb="popover"] ul,
            div[data-baseweb="menu"] {
                background-color: white !important;
            }

            div[data-baseweb="popover"] li,
            div[data-baseweb="menu"] li {
                background-color: white !important;
                color: #333333 !important;
            }

            div[data-baseweb="popover"] li:hover,
            div[data-baseweb="menu"] li:hover {
                background-color: #E0E3FF !important;
                color: #333333 !important;
            }

            div[data-baseweb="popover"] li[aria-selected="true"] {
                background-color: #5865F2 !important;
                color: white !important;
            }

            /* Selectbox input box */
            div[data-baseweb="select"] {
                background-color: white !important;
                border-radius: 0.75rem !important;
            }

            div[data-baseweb="select"] div,
            div[data-baseweb="select"] span,
            div[data-baseweb="select"] input {
                background-color: white !important;
                color: #333333 !important;
            }

            /* File uploader */
            [data-testid="stFileUploader"] {
                background-color: white !important;
                border-radius: 0.75rem !important;
                color: #333333 !important;
            }

            /* Camera input */
            [data-testid="stCameraInput"] {
                background-color: white !important;
                border-radius: 0.75rem !important;
            }

            /* Dataframe */
            [data-testid="stDataFrame"] {
                background-color: white !important;
                color: #333333 !important;
            }

            /* Spinner text */
            [data-testid="stSpinner"] p {
                color: #5865F2 !important;
            }

            /* Success / Info / Warning / Error boxes */
            [data-testid="stAlert"] {
                background-color: white !important;
                color: #333333 !important;
                border-radius: 0.75rem !important;
            }

            [data-testid="stAlert"] p {
                color: inherit !important;
            }

            /* Dialog / Modal */
            [data-testid="stDialog"] > div,
            div[role="dialog"] {
                background-color: white !important;
            }

            [data-testid="stDialog"] h1,
            [data-testid="stDialog"] h2,
            [data-testid="stDialog"] h3 {
                font-family: 'Climate Crisis', sans-serif !important;
                color: #1a1a1a !important;
            }

            [data-testid="stDialog"] p,
            [data-testid="stDialog"] li,
            [data-testid="stDialog"] label {
                font-family: 'Outfit', sans-serif !important;
                color: #333333 !important;
            }

            [data-testid="stDialog"] button * {
                color: white !important;
            }

            /* Code blocks inside dialog */
            [data-testid="stDialog"] pre,
            [data-testid="stDialog"] code {
                background-color: #f0f0f0 !important;
                color: #333333 !important;
            }

            /* Toast notifications */
            [data-testid="stToast"] {
                background-color: #1a1a1a !important;
                border-radius: 1rem !important;
            }
            [data-testid="stToast"] p,
            [data-testid="stToast"] * {
                color: white !important;
            }

            h3, h4 {
                color: #333333 !important;
            }

            /* Subheader */
            [data-testid="stHeadingWithActionElements"] h3 {
                color: #5865F2 !important;
            }

            /* Selectbox, radio, checkbox labels */
            [data-testid="stWidgetLabel"] p {
                color: #5865F2 !important;
            }

            /* Divider */
            hr {
                border-color: #5865F2 !important;
                opacity: 0.3 !important;
            }
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
            }
                

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
                color: #1a1a1a !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
            }
                

            button{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }


            div[data-baseweb="input"], div[data-baseweb="textarea"] {
                background-color: white !important;
                border-radius: 0.75rem !important;
            }

            div[data-baseweb="input"] input,
            div[data-baseweb="textarea"] textarea {
                background-color: white !important;
                color: #333333 !important;
                caret-color: #333333 !important;
            }

            div[data-baseweb="input"] input::placeholder,
            div[data-baseweb="textarea"] textarea::placeholder {
                color: #aaaaaa !important;
            }

            div[data-testid="stTextInput"] label,
            div[data-testid="stTextArea"] label {
                color: #5865F2 !important;
                font-family: 'Outfit', sans-serif !important;
            }
            button:hover{
                transform :scale(1.05)}
        </style>  

                """
            ,unsafe_allow_html=True)