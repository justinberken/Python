This code exports selected solids in Rhino 3D to the ".stp" file format.
Requirements

    Rhino 3D
    RhinoScript library

Usage

    Open a Rhino 3D model and select the solids you want to export.
    Run the code.
    Each selected solid will be exported to its own separate ".stp" file in the "C:\ExportedSolids\" directory.

Note

    If a solid doesn't have a name, a default name with a numeric suffix will be assigned to it to avoid overwriting files with the same name.
    All objects will be unselected before each solid is selected and exported.

License

This code is open-source software licensed under the MIT License.
