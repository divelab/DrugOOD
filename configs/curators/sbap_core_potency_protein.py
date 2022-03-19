_base_ = ['../_base_/curators/sbap_defaults.py',
          '../_base_/curators/noises/core.py',
          '../_base_/curators/domains/protein.py']

path = dict(task=dict(subset="sbap_core_potency_protein"))

noise_filter = dict(assay=dict(measurement_type=['Potency'], assay_target_type=["SINGLE PROTEIN"]))
