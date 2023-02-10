# Import the RhinoScript library
import rhinoscriptsyntax as rs

# Get a list of the selected solids in the Rhino model
selected_solids = rs.SelectedObjects()

# Counter to keep track of the number of unnamed solids
counter = 1

# Loop through each solid in the list of selected solids
for solid in selected_solids:
    # Get the name of the solid
    solid_name = rs.ObjectName(solid)
    
    # If the solid name is None, use a default name with a numeric suffix for the export file
    if solid_name is None:
        solid_name = "NoName" + str(counter)
        counter += 1
    
    # Concatenate the solid name with the export path to create the export file path
    export_path = "C:\\ExportedSolids\\" + solid_name + ".stp"
    
    # Unselect all objects
    rs.UnselectAllObjects()
    
    # Select the solid
    rs.SelectObject(solid)
    
    # Export the selected solid to the specified file path in the ".stp" file format
    rs.Command("_-Export " + export_path + " _Enter")
