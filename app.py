import streamlit as st
from eigen_value_power_method import eigen_value_power_method
from qr_household import house_holder_method


def main():
    st.title('Basic Forms')

    menu = ['Eigen Value (Power Method)', 'QR Householder Method']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Eigen Value (Power Method)':
        st.subheader('Eigen Value (Power Method)')
        eigen_value_power_method()
    if choice == 'QR Householder Method':
        st.subheader('QR Householder Method')
        house_holder_method()


if __name__ == '__main__':
    main()
