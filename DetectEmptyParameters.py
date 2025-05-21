import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitAPI')
clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

from Autodesk.Revit.DB import *
from System.Collections.Generic import List  # Import List

# Get the current Revit document
doc = DocumentManager.Instance.CurrentDBDocument
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

# Input - elements to check and select (IN[0])
elements = UnwrapElement(IN[0])

# Input - list of parameters or parameter pairs (IN[1])
parameter_pairs = IN[1]

# Collection of elements with empty parameters
elements_with_empty_parameters = []

# Iterate through each element
for element in elements:
    should_select = False
    for pair in parameter_pairs:
        if isinstance(pair, list) and len(pair) > 0:
            source_param = pair[0]
            if len(pair) > 1:
                target_param = pair[1]
            else:
                target_param = None

            # Get value of the source parameter
            source = element.LookupParameter(source_param)
            if source:
                source_value = source.AsString()

                # If the parameter value is empty, mark for selection
                if not source_value:
                    should_select = True
                    break

    # Add element to the list if any parameter is empty
    if should_select:
        elements_with_empty_parameters.append(element)

# Output (optional)
OUT = elements_with_empty_parameters
