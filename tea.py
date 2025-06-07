import streamlit as st

st.title("حاسبة الشاي والسكر حسب كمية الماء")

# إدخال كمية الماء
water_ml = st.number_input("أدخل كمية الماء (بالمليلتر):", min_value=1)

# الحسابات
if water_ml:
    tea = (water_ml * 7.05) / 500
    sugar = (water_ml * 22.45) / 500

    st.write(f"🔸 كمية الشاي المناسبة: **{tea:.2f} غرام**")
    st.write(f"🔸 كمية السكر المناسبة: **{sugar:.2f} غرام**")
