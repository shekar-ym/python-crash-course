from printing_functions import printing_models as pm
from printing_functions import summarize_print as sp

unprinted_designs = ['phone case', 'glasses','pen holder']
completed_models = []

pm(unprinted_designs, completed_models)
sp(completed_models)

