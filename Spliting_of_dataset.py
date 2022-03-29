import splitfolders  # or import split_folders

input_folder = 'input_folder_name/'#please put the main folder name here

# Split with a ratio.
#To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
splitfolders.ratio(input_folder, output="main_output_folder_name",seed=please_fill_random_seed_number, ratio=(train ration(e.g. .7), val ration(e.g. .3)), group_prefix=None) # default values

#Train, val, test
#splitfolders.ratio(input_folder, output="tomato_new",seed=42, ratio=(.7, .2, .1), group_prefix=None) # default values

