def printing_models(unprinted_designs, completed_models):
    """This function prints the models in the list unprinted_designs"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def summarize_print(completed_models):
    """This function summarizes the pringting job"""
    print("Printing of following models is completed")
    for completed_model in completed_models:
        print(completed_model)