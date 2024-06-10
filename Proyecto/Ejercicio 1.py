'''
Determine the mean and standard deviation per loss for a Pareto distribution with
a = 3 and È = 2,000 with a deductible of 500 and a policy limit of 2,500. Note that
the maximum covered loss is u = 3,000.
'''
import numpy as np
import scipy.stats as stats
import scipy.integrate as integrate

# Parámetros de la distribución de Pareto
a = 3
theta = 2000

# Deducible y límite de póliza
d = 500
L = 2500
u = 3000

# Distribución de Pareto con scipy
pareto_dist = stats.pareto(b=a, scale=theta)

# Función de densidad (pdf) de Pareto
def pareto_pdf(x):
    return pareto_dist.pdf(x)

# Media ajustada por el deducible y el límite de póliza
def expected_value(d, L):
    integral, _ = integrate.quad(lambda x: (x - d) * pareto_pdf(x), d, d + L)
    return integral

# Varianza ajustada por el deducible y el límite de póliza
def variance(d, L):
    integral_2, _ = integrate.quad(lambda x: ((x - d) ** 2) * pareto_pdf(x), d, d + L)
    expected = expected_value(d, L)
    var = integral_2 - expected ** 2
    return var

# Cálculo de la media y la desviación estándar
mean = expected_value(d, L)
var = variance(d, L)
std_dev = np.sqrt(var)

# Imprimir los resultados
print("Media:", mean)
print("Varianza:", var)
print("Desviación estándar:", std_dev)
