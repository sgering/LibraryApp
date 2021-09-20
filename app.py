import streamlit as st
import webbrowser

#Configuration
#------------------------------------------------------------
libraries ="""https://clamsnet.overdrive.com/clamsnet-visitor/content/search?query=
https://bpl.overdrive.com/bpl-visitor/content/search?query=
https://mvlc.overdrive.com/mvlc-visitor/content/search?query=
https://noble.overdrive.com/noble-visitor/content/search?query=
https://ocln.overdrive.com/ocln-visitor/content/search?query=
https://sails.overdrive.com/sails-visitor/content/search?query=
https://acld.overdrive.com/acld-visitor/content/search?query=
https://lltc.overdrive.com/lltc-visitor/content/search?query=
https://tempe.overdrive.com/tempe-visitor/content/search?query=
https://ccld.overdrive.com/ccld-visitor/content/search?query=
https://navajoco.overdrive.com/navajoco-visitor/content/search?query=
https://yln.overdrive.com/yln-visitor/content/search?query=
https://cocolib.overdrive.com/cocolib-visitor/content/search?query=
https://svlc.overdrive.com/svlc-visitor/content/search?query=
https://yuma.overdrive.com/yuma-visitor/content/search?query=
https://minuteman.overdrive.com/minuteman-visitor/content/search?query=
https://pima.overdrive.com/search?query="""

#Styling
#----------------------------------------------------

padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
        primaryColor="#2214c7";
        backgroundColor="#ffffff";
        secondaryBackgroundColor="#e8eef9";
        textColor="#000000";
        font="sans serif"

    }} </style> """, unsafe_allow_html=True)

#Maincode
#----------------------------------------------------

title = st.text_input('Book title, subject, or keyword', 'Mystery')

#library_list = st.text_area("Libraries",libraries,height=500)

if st.button('Search'):

    liblist = libraries.splitlines()
    for lib in liblist:
        query = lib + '%s' %title
        #webbrowser.open(query)  # Go to example.com
        st.write(query)
       
    



