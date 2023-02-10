# Import the RhinoScript and os libraries
import rhinoscriptsyntax as rs
import os

# Prompt the user to enter the directory containing the .stp files
stp_directory = rs.GetString("Enter the directory containing the .stp files")

try:
    # Get a list of all .stp files in the directory
    stp_files = [f for f in os.listdir(stp_directory) if f.endswith(".stp")]

    # Loop through each .stp file in the list
    for stp_file in stp_files:
        # Create the full file path
        stp_file_path = os.path.join(stp_directory, stp_file)

        # Import the .stp file into the Rhino model
        rs.Command("_-Import " + stp_file_path + " _Enter")

except WindowsError:
    print("Error accessing directory: " + stp_directory)
