import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("ggplot")

def formato(num):
    if num%1 == 0:
        return int(num)
    else:
        return num

st.title(":blue[Ecuaciones cuadraticas]") 
st.header("¿Qué es una ecuación cuadratica?")
st.markdown("Una ecuación cuadrática, también conocida como ecuación de segundo grado, es una ecuación polinómica donde se tiene un termino cuadratico, uno lineal y otro constante.")
st.markdown("que se puede escribir en la forma general:")
st.latex("ax^2 + bx + c = 0")
st.markdown("Este polinomio se puede interpretar igualmente que una función cuadratica, es decir por una parabola. Esta grafica es útil porque las abscisas de las intersecciones, en el caso de existir con el eje x son las raices reales de la ecuación.")

st.markdown("**Condiciones que debe cumplir una ecuación cuadratica:**")
st.markdown("""
- Los valores a, b y c deben ser conocidos.
- La a no puede ser igual a 0.
""")
st.subheader("Formula general para la ecuación cuadratica:")
st.latex("x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}")

st.markdown("Esta fórmula es muy útil ya que solo debemos reemplazar los valores que nos den en la formula.")
st.subheader("El discriminante:")
st.markdown("""
El discriminante, representado como (b^2 - 4ac) es muy importante ya que con este podemos saber que tipo de respuestas tendrá la ecuación, por ejemplo:
- Si el discriminate es positivo, la ecuación tendrá dos soluciones.
- Si es negativo, la ecuación no tendrá soluciones reales.
- Si es igual a 0, la ecuación tiene una única solución.
""")

st.subheader(":blue[Resolviendo una ecuación cuadratica con la formula general:]")
st.markdown("Para resolverla, solo pon los valores de a,b y c para hacer los cálculos.")

with st.container(border=True):
    st.markdown("Digite la ecuación: ")  
    col1, col2, col3 = st.columns(3)
    with col1:
        a = float(st.number_input("a"))
    with col2:
        b = float(st.number_input("b"))
    with col3:
        c = float(st.number_input("c"))
st.markdown("La ecuacion ingresada es:")
st.latex(f"{formato(a)}x^2 + {formato(b)}x + {formato(c)} = 0")

dn = (b)*(b)-4*(a)*(c)
if dn < 0:
    st.markdown("la ecuación no tiene soluciones reales")
elif dn == 0:
    x1 = (f" -{formato(b)}/2*{formato(a)} ")
    st.markdown(f"""
    La ecuación tiene una única solución:
    $$
    x = {x1}
    $$
    """)
else:
    x1 = (f" -{formato(b)} +\\sqrt[2]{formato(dn)}/2*{formato(a)} ")

    x2 = (f" -{formato(b)} -\\sqrt[2]{formato(dn)}/2*{formato(a)} ")
    st.markdown(f"""
    La ecuación tiene dos soluciones:
    $$
    x_1 = \\frac{{-({formato(b)} + \\sqrt({formato(b)})^2 - 4({formato(a)})({formato(c)})}} {{2({formato(a)})}} = {x1}
    $$

    $$
    x_2 =  \\frac{{-({formato(b)} - \\sqrt({formato(b)})^2 - 4({formato(a)})({formato(c)})}} {{2({formato(a)})}} = {x2}
    $$
    """)

with st.container(border=True):
    col_1, col_2 = st.columns([3, 1], gap= "medium")
    with col_1:
        if dn != 0:
            ini = - 5
            fin = + 5
        else: 
            ini = - 5
            fin = + 5

        x = np.linspace(ini, fin, 150)
        y = a*x**2 + b*x + c

        fig, ax = plt.subplots()

        ax.plot(x, y, label = f"${formato(a)}x^2 + {formato(b)}x + {formato(c)} = 0$")
        plt.title("Grafica de la ecuación")
        plt.xlabel("x")
        plt.ylabel("y")
        st.pyplot(fig)

    with col_2:
        if dn < 0:
            st.markdown("""
        >Observe que la parabola no toca el eje x, por ende significa que no tiene soluciones reales.
        """)
        elif dn == 0:
            st.markdown("""
        >Observe que la parabola toca el eje x en un solo punto, por ende significa que tiene una única solución.
        """)
        else:
            st.markdown("""
        >Observe que la parabola toca el eje x en dos puntos, por ende significa que tiene dos soluciones.
        """)
    



