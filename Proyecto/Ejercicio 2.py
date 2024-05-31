'''
A group life insurance policy has an accidental death rider. For ordinary deaths, the
benefit is 10,000; however, for accidental deaths, the benefit is 20,000. The insureds are
approximately the same age, so it is reasonable to assume they all have the same claim
probabilities. Let them be 0.97 for no claim, 0.01 for an ordinary death claim, and 0.02
for an accidental death claim. A reinsurer has been asked to bid on providing an excess
reinsurance that will pay 10,000 for each accidental death.
(a) The claim process can be modeled with a frequency component that has the
Bernoulli distribution (the event is claim/no claim) and a two-point severity component
(the probabilities are associated with the two claim levels, given that a
claim occurred). Specify the probability distributions for the frequency and severity
random variables.
(b) Suppose the reinsurer wants to retain the same frequency distribution. Determine
the modified severity distribution that will reflect the reinsurer's payments.
(c) Determine the reinsurer's frequency and severity distributions when the severity
distribution is to be conditional on a reinsurance payment being made.
'''


import numpy as np

# (a) Frecuencia y severidad
# Frecuencia: Bernoulli(0.03) - no reclamo = 0.97, reclamo = 0.03
prob_no_claim = 0.97
prob_claim = 0.03

# Severidad, dado que hay un reclamo
prob_muerte_ordinaria_dado_reclamo = 0.01 / 0.03
prob_muerte_accidental_dado_reclamo = 0.02 / 0.03
distribucion_severidad = {
    'muerte_ordinaria': (10000, prob_muerte_ordinaria_dado_reclamo),
    'muerte_accidental': (20000, prob_muerte_accidental_dado_reclamo)
}

# (b) Severidad modificada para el reasegurador
distribucion_severidad_reasegurador = {
    'muerte_ordinaria': (0, prob_muerte_ordinaria_dado_reclamo),
    'muerte_accidental': (10000, prob_muerte_accidental_dado_reclamo)
}

# (c) Frecuencia y severidad del reasegurador
prob_no_pago_reasegurador = 0.98  # 0.97 (no reclamo) + 0.01 (muerte ordinaria)
prob_pago_reasegurador = 0.02

# Severidad dada el pago de reaseguro
distribucion_severidad_condicional_reasegurador = {
    'sin_pago': (0, 0),
    'con_pago': (10000, 1)
}

# Mostrar los resultados
print("Frecuencia (Bernoulli) - No reclamo:", prob_no_claim)
print("Frecuencia (Bernoulli) - Reclamo:", prob_claim)
print("\nSeveridad dado un reclamo:")
print(distribucion_severidad)

print("\nSeveridad modificada para el reasegurador:")
print(distribucion_severidad_reasegurador)

print("\nFrecuencia del reasegurador (Bernoulli):")
print("Sin pago:", prob_no_pago_reasegurador)
print("Con pago:", prob_pago_reasegurador)

print("\nSeveridad del reasegurador dada un pago de reaseguro:")
print(distribucion_severidad_condicional_reasegurador)
