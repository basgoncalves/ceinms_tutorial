template = 'Results_SO_and_MA_{subject}_StaticOptimization_force.sto'

# Using named arguments
subject_string_format = template.format(subject='003')
print(f"Using .format() with named argument: {subject_string_format}")